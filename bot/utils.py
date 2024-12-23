import re


def escape_markdown(text: str) -> str:

    special_chars = r"([\\`*_{}\[\]()#+.!|-])"
    return re.sub(special_chars, r"\\\1", text)


def format_response_as_markdown(data: dict) -> str:

    model_response = data.get("model_response", "")
    sources = data.get("sources", [])

    markdown_response = escape_markdown(model_response).replace("\n", "  \n")

    for source in sources:
        title = escape_markdown(source.get("title", "Titulo desconocido"))
        pages = escape_markdown(", ".join(map(str, source.get("pages", []))))
        author = escape_markdown(source.get("author", "Autor desconocido"))
        link = source.get("link", "#")
        year = source.get("year", "Año desconocido")

        source_line = f"\\([{author}]({link}), pp\\. {pages}\\)"

        markdown_response += f"  \n{source_line}"

    return markdown_response
