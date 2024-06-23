import functools
from pathlib import Path

from langchain.globals import set_llm_cache
from langchain_community.cache import SQLiteCache
from langchain_community.document_loaders.html_bs import BSHTMLLoader
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_core.messages import AIMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSerializable
from langchain_openai import ChatOpenAI

database_path = Path.home() / ".cache" / ".langchain.db"
cache = SQLiteCache(database_path.as_posix())
set_llm_cache(cache)


PROMPT_TEMPLATE = """Write a concise summary in bullet points using {lang} for the following article:
{text}

Summary:"""


@functools.cache
def get_chain() -> RunnableSerializable:
    llm = ChatOpenAI(temperature=0, model="gpt-4o")
    prompt = PromptTemplate.from_template(PROMPT_TEMPLATE)
    chain = prompt | llm
    return chain


def load_html(f: str) -> str:
    loader = BSHTMLLoader(f)
    docs = loader.load()
    return "\n".join([doc.page_content for doc in docs])


def load_pdf(f: str) -> str:
    loader = PyPDFLoader(f)
    docs = loader.load()
    return "\n".join([doc.page_content for doc in docs])


def summarize(text: str, lang: str = "English") -> str:
    chain = get_chain()
    ai_message: AIMessage = chain.invoke({"text": text, "lang": lang})
    return ai_message.pretty_repr()
