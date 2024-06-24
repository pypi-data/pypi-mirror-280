import os
from typing import List
from typing import Union

import openai
import tiktoken
from dotenv import load_dotenv
from icecream import ic
from langchain_text_splitters import RecursiveCharacterTextSplitter


load_dotenv()  # read local .env file
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MAX_TOKENS_PER_CHUNK = (
    1000  # if text is more than this many tokens, we'll break it up into
)
# discrete chunks to revise one chunk at a time


def get_completion(
    prompt: str,
    system_message: str = "You are a helpful assistant.",
    model: str = "gpt-4o",
    temperature: float = 0.3,
    json_mode: bool = False,
) -> Union[str, dict]:
    """
        Generate a completion using the OpenAI API.

    Args:
        prompt (str): The user's prompt or query.
        system_message (str, optional): The system message to set the context for the assistant.
            Defaults to "You are a helpful assistant.".
        model (str, optional): The name of the OpenAI model to use for generating the completion.
            Defaults to "gpt-4o".
        temperature (float, optional): The sampling temperature for controlling the randomness of the generated text.
            Defaults to 0.3.
        json_mode (bool, optional): Whether to return the response in JSON format.
            Defaults to False.

    Returns:
        Union[str, dict]: The generated completion.
            If json_mode is True, returns the complete API response as a dictionary.
            If json_mode is False, returns the generated text as a string.
    """

    if json_mode:
        response = client.chat.completions.create(
            model=model,
            temperature=temperature,
            top_p=1,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content
    else:
        response = client.chat.completions.create(
            model=model,
            temperature=temperature,
            top_p=1,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content


def one_chunk_initial_revision(
    draft: str
) -> str:
    """
    Revise the entire text as one chunk using an LLM.

    Args:
        draft (str): The text to be revised.

    Returns:
        str: The revised text.
    """

    system_message = f"You are an expert linguist, specializing in academic English editing."

    revision_prompt = f"""This is a draft to be revised, please provide the revision for this text. \
Reorganize the paragraphs and sentences to ensure coherence, while enhancing logical flow and readability. \
Do not provide any explanations or text apart from the revision.
{draft}

Revised text:"""

    prompt = revision_prompt.format(draft=draft)

    revision = get_completion(prompt, system_message=system_message)

    return revision


def one_chunk_reflect_on_revision(
    draft: str,
    revision_1: str,
) -> str:
    """
    Use an LLM to reflect on the revision, treating the entire text as one chunk.

    Args:
        draft (str): The original text.
        revision_1 (str): The initial revision of the draft.

    Returns:
        str: The LLM's reflection on the revision, providing constructive criticism and suggestions for improvement.
    """

    system_message = f"You are an expert linguist specializing in academic English editing. \
You will be provided with a draft and its revision and your goal is to improve the revision."

    reflection_prompt = f"""Your task is to carefully read a draft and a revision, and then give constructive criticism and helpful suggestions to improve the revision. \
The final style and tone of the revision should match the academic style in English.

The draft and initial revision, delimited by XML tags <DRAFT></DRAFT> and <REVISION></REVISION>, are as follows:

<DRAFT>
{draft}
</DRAFT>

<REVISION>
{revision_1}
</REVISION>

When writing suggestions, pay attention to whether there are ways to improve the revision's \n\
(i) accuracy (by correcting errors of addition, miscorrection, omission, or unrevised text),\n\
(ii) fluency (by applying English grammar, spelling and punctuation rules, and ensuring there are no unnecessary repetitions),\n\
(iii) style (by ensuring the revisions reflect the style of the draft and takes into account any cultural context),\n\
(iv) terminology (by ensuring terminology use is consistent and reflects the draft domain; and by only ensuring you use equivalent idioms English).\n\

Write a list of specific, helpful and constructive suggestions for improving the revision.
Each suggestion should address one specific part of the revision.
Output only the suggestions and nothing else."""

    prompt = reflection_prompt.format(
        draft=draft,
        revision_1=revision_1,
    )
    reflection = get_completion(prompt, system_message=system_message)
    return reflection


def one_chunk_improve_revision(
    draft: str,
    revision_1: str,
    reflection: str,
) -> str:
    """
    Use the reflection to improve the revision, treating the entire text as one chunk.

    Args:
        draft (str): The original text.
        revision_1 (str): The initial revision of the draft.
        reflection (str): Expert suggestions and constructive criticism for improving the revision.

    Returns:
        str: The improved revision based on the expert suggestions.
    """

    system_message = f"You are an expert linguist, specializing in academic English editing."

    prompt = f"""Your task is to carefully read, then edit, a revision, taking into account a list of expert suggestions and constructive criticisms. \
The final style and tone of the revision should match the academic style in English.

The draft, the initial revision, and the expert linguist suggestions are delimited by XML tags <DRAFT></DRAFT>, <REVISION></REVISION> and <EXPERT_SUGGESTIONS></EXPERT_SUGGESTIONS> \
as follows:

<DRAFT>
{draft}
</DRAFT>

<REVISION>
{revision_1}
</REVISION>

<EXPERT_SUGGESTIONS>
{reflection}
</EXPERT_SUGGESTIONS>

Please take into account the expert suggestions when editing the revision. Edit the revision by ensuring:

(i) accuracy (by correcting errors of addition, miscorrection, omission, or unrevised text),
(ii) fluency (by applying English grammar, spelling and punctuation rules and ensuring there are no unnecessary repetitions), \
(iii) style (by ensuring the revisions reflect the style of the draft)
(iv) terminology (inappropriate for context, inconsistent use), or
(v) other errors.

Output only the new revision and nothing else."""

    revision_2 = get_completion(prompt, system_message)

    return revision_2


def one_chunk_revise_text(
    draft: str
) -> str:
    """
    Revise a single chunk of text.

    This function performs a two-step revision process:
    1. Get an initial revision of the draft.
    2. Reflect on the initial revision and generate an improved revision.

    Args:
        draft (str): The text to be revised.
    Returns:
        str: The improved revision of the draft.
    """
    revision_1 = one_chunk_initial_revision(
        draft
    )

    reflection = one_chunk_reflect_on_revision(
        draft, revision_1
    )
    revision_2 = one_chunk_improve_revision(
        draft, revision_1, reflection
    )

    return revision_2


def num_tokens_in_string(
    input_str: str, encoding_name: str = "cl100k_base"
) -> int:
    """
    Calculate the number of tokens in a given string using a specified encoding.

    Args:
        str (str): The input string to be tokenized.
        encoding_name (str, optional): The name of the encoding to use. Defaults to "cl100k_base",
            which is the most commonly used encoder (used by GPT-4).

    Returns:
        int: The number of tokens in the input string.

    Example:
        >>> text = "Hello, how are you?"
        >>> num_tokens = num_tokens_in_string(text)
        >>> print(num_tokens)
        5
    """
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(input_str))
    return num_tokens


def multichunk_initial_revision(
    draft_chunks: List[str]
) -> List[str]:
    """
    Revise a text in multiple chunks.

    Args:
        draft_chunks (List[str]): A list of text chunks to be revised.

    Returns:
        List[str]: A list of revised text chunks.
    """

    system_message = f"You are an expert linguist, specializing in academic English editing."

    revision_prompt = """Your task is to provide a professional revision of PART of a text. \
Reorganize the paragraphs and sentences to ensure coherence, while enhancing logical flow and readability.

The draft is below, delimited by XML tags <DRAFT> and </DRAFT>. Revise only the part within the draft
delimited by <REVISE_THIS> and </REVISE_THIS>. You can use the rest of the draft as context, but do not revise any
of the other text. Do not output anything other than the revision of the indicated part of the text.

<DRAFT>
{tagged_text}
</DRAFT>

To reiterate, you should revise only this part of the text, shown here again between <REVISE_THIS> and </REVISE_THIS>:
<REVISE_THIS>
{chunk_to_revise}
</REVISE_THIS>

Output only the revision of the portion you are asked to revise, and nothing else.
"""

    revision_chunks = []
    for i in range(len(draft_chunks)):
        # Will revise chunk i
        tagged_text = (
            "".join(draft_chunks[0:i])
            + "<REVISE_THIS>"
            + draft_chunks[i]
            + "</REVISE_THIS>"
            + "".join(draft_chunks[i + 1 :])
        )

        prompt = revision_prompt.format(
            tagged_text=tagged_text,
            chunk_to_revise=draft_chunks[i],
        )

        revision = get_completion(prompt, system_message=system_message)
        revision_chunks.append(revision)

    return revision_chunks


def multichunk_reflect_on_revision(
    draft_chunks: List[str],
    revision_1_chunks: List[str],
) -> List[str]:
    """
    Provides constructive criticism and suggestions for improving a partial revision.

    Args:
        draft_chunks (List[str]): The draft divided into chunks.
        revision_1_chunks (List[str]): The revised chunks corresponding to the draft chunks.

    Returns:
        List[str]: A list of reflections containing suggestions for improving each revised chunk.
    """

    system_message = f"You are an expert linguist, specializing in academic English editing. \
You will be provided with a draft and its revision and your goal is to improve the revision."

    reflection_prompt = """Your task is to carefully read a draft and part of a revision of that text, and then give constructive criticism and helpful suggestions for improving the revision. \
The final style and tone of the revision should match the academic style in English.

The draft is below, delimited by XML tags <DRAFT> and </DRAFT>, and the part that has been revised
is delimited by <REVISE_THIS> and </REVISE_THIS> within the draft. You can use the rest of the draft
as context for critiquing the revised part.

<DRAFT>
{tagged_text}
</DRAFT>

To reiterate, only part of the text is being revised, shown here again between <REVISE_THIS> and </REVISE_THIS>:
<REVISE_THIS>
{chunk_to_revise}
</REVISE_THIS>

The revision of the indicated part, delimited below by <REVISION> and </REVISION>, is as follows:
<REVISION>
{revision_1_chunk}
</REVISION>

When writing suggestions, pay attention to whether there are ways to improve the revision's:\n\
(i) accuracy (by correcting errors of addition, miscorrection, omission, or unrevised text),\n\
(ii) fluency (by applying English grammar, spelling and punctuation rules, and ensuring there are no unnecessary repetitions),\n\
(iii) style (by ensuring the revisions reflect the style of the draft and takes into account any cultural context),\n\
(iv) terminology (by ensuring terminology use is consistent and reflects the draft domain; and by only ensuring you use equivalent idioms English).\n\

Write a list of specific, helpful and constructive suggestions for improving the revision.
Each suggestion should address one specific part of the revision.
Output only the suggestions and nothing else."""

    reflection_chunks = []
    for i in range(len(draft_chunks)):
        # Will revise chunk i
        tagged_text = (
            "".join(draft_chunks[0:i])
            + "<REVISE_THIS>"
            + draft_chunks[i]
            + "</REVISE_THIS>"
            + "".join(draft_chunks[i + 1 :])
        )

        prompt = reflection_prompt.format(
            tagged_text=tagged_text,
            chunk_to_revise=draft_chunks[i],
            revision_1_chunk=revision_1_chunks[i],
        )

        reflection = get_completion(prompt, system_message=system_message)
        reflection_chunks.append(reflection)

    return reflection_chunks


def multichunk_improve_revision(
    draft_chunks: List[str],
    revision_1_chunks: List[str],
    reflection_chunks: List[str],
) -> List[str]:
    """
    Improves the revision of a text by considering expert suggestions.

    Args:
        draft_chunks (List[str]): The draft divided into chunks.
        revision_1_chunks (List[str]): The initial revision of each chunk.
        reflection_chunks (List[str]): Expert suggestions for improving each revised chunk.

    Returns:
        List[str]: The improved revision of each chunk.
    """

    system_message = f"You are an expert linguist, specializing in academic English editing."

    improvement_prompt = """Your task is to carefully read, then improve, a revision, taking into account a set of expert suggestions and constructive critisms.
The final style and tone of the revision should match the academic style in English. Below, the draft, initial revision, and expert suggestions are provided.

The draft is below, delimited by XML tags <DRAFT> and </DRAFT>, and the part that has been revised
is delimited by <REVISE_THIS> and </REVISE_THIS> within the draft. You can use the rest of the draft
as context, but need to provide a revision only of the part indicated by <REVISE_THIS> and </REVISE_THIS>.

<DRAFT>
{tagged_text}
</DRAFT>

To reiterate, only part of the text is being revised, shown here again between <REVISE_THIS> and </REVISE_THIS>:
<REVISE_THIS>
{chunk_to_revise}
</REVISE_THIS>

The revision of the indicated part, delimited below by <REVISION> and </REVISION>, is as follows:
<REVISION>
{revision_1_chunk}
</REVISION>

The expert suggestions of the indicated part, delimited below by <EXPERT_SUGGESTIONS> and </EXPERT_SUGGESTIONS>, is as follows:
<EXPERT_SUGGESTIONS>
{reflection_chunk}
</EXPERT_SUGGESTIONS>

Taking into account the expert suggestions rewrite the revision to improve it, paying attention
to whether there are ways to improve the revision's

(i) accuracy (by correcting errors of addition, miscorrection, omission, or unrevised text),
(ii) fluency (by applying English grammar, spelling and punctuation rules and ensuring there are no unnecessary repetitions), \
(iii) style (by ensuring the revisions reflect the style of the draft)
(iv) terminology (inappropriate for context, inconsistent use), or
(v) other errors.

Output only the new revision of the indicated part and nothing else."""

    revision_2_chunks = []
    for i in range(len(draft_chunks)):
        # Will revise chunk i
        tagged_text = (
            "".join(draft_chunks[0:i])
            + "<REVISE_THIS>"
            + draft_chunks[i]
            + "</REVISE_THIS>"
            + "".join(draft_chunks[i + 1 :])
        )

        prompt = improvement_prompt.format(
            tagged_text=tagged_text,
            chunk_to_revise=draft_chunks[i],
            revision_1_chunk=revision_1_chunks[i],
            reflection_chunk=reflection_chunks[i],
        )

        revision_2 = get_completion(prompt, system_message=system_message)
        revision_2_chunks.append(revision_2)

    return revision_2_chunks


def multichunk_revision(
    draft_chunks
):
    """
    Improves the revision of multiple text chunks based on the initial revision and reflection.

    Args:
        draft_chunks (List[str]): The list of draft chunks to be revised.
        revision_1_chunks (List[str]): The list of initial revisions for each draft chunk.
        reflection_chunks (List[str]): The list of reflections on the initial revisions.
    Returns:
        List[str]: The list of improved revisions for each draft chunk.
    """

    revision_1_chunks = multichunk_initial_revision(
        draft_chunks
    )

    reflection_chunks = multichunk_reflect_on_revision(
        draft_chunks, revision_1_chunks
    )

    revision_2_chunks = multichunk_improve_revision(
        draft_chunks, revision_1_chunks, reflection_chunks
    )

    return revision_2_chunks


def calculate_chunk_size(token_count: int, token_limit: int) -> int:
    """
    Calculate the chunk size based on the token count and token limit.

    Args:
        token_count (int): The total number of tokens.
        token_limit (int): The maximum number of tokens allowed per chunk.

    Returns:
        int: The calculated chunk size.

    Description:
        This function calculates the chunk size based on the given token count and token limit.
        If the token count is less than or equal to the token limit, the function returns the token count as the chunk size.
        Otherwise, it calculates the number of chunks needed to accommodate all the tokens within the token limit.
        The chunk size is determined by dividing the token limit by the number of chunks.
        If there are remaining tokens after dividing the token count by the token limit,
        the chunk size is adjusted by adding the remaining tokens divided by the number of chunks.

    Example:
        >>> calculate_chunk_size(1000, 500)
        500
        >>> calculate_chunk_size(1530, 500)
        389
        >>> calculate_chunk_size(2242, 500)
        496
    """

    if token_count <= token_limit:
        return token_count

    num_chunks = (token_count + token_limit - 1) // token_limit
    chunk_size = token_count // num_chunks

    remaining_tokens = token_count % token_limit
    if remaining_tokens > 0:
        chunk_size += remaining_tokens // num_chunks

    return chunk_size


def revise(
    draft,
    max_tokens=MAX_TOKENS_PER_CHUNK,
):
    """Revise the draft."""

    num_tokens_in_text = num_tokens_in_string(draft)

    ic(num_tokens_in_text)

    if num_tokens_in_text < max_tokens:
        ic("Revising text as single chunk")

        final_revision = one_chunk_revise_text(
            draft
        )

        return final_revision

    else:
        ic("Revising text as multiple chunks")

        token_size = calculate_chunk_size(
            token_count=num_tokens_in_text, token_limit=max_tokens
        )

        ic(token_size)

        text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            model_name="gpt-4",
            chunk_size=token_size,
            chunk_overlap=0,
        )

        draft_chunks = text_splitter.split_text(draft)

        revision_2_chunks = multichunk_revision(
            draft_chunks
        )

        return "".join(revision_2_chunks)
