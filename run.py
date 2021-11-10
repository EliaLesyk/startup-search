import json

import requests
import streamlit as st


#import streamlit.components.v1 as components


def get_text(name: str, description: str):
    return f"{name}[SEP]{description}"


def search(description: str, host: str) -> dict:
    text = get_text("", description)
    data = '{"data":[{"text": "' + text + '"}]}'

    content = requests.post(
        f"{host}/search",
        headers={
            "Content-Type": "application/json",
        },
        data=data,
    ).json()

    doc = content["data"]["docs"][0]

    return doc


def finetune(doc: dict, match: dict, relevant: bool, host: str) -> dict:
    labeled = doc.copy()
    labeled["tags"]["finetuner"] = {"label": 1 if relevant else -1}
    match["tags"]["finetuner"] = {"label": 1 if relevant else -1}
    labeled["matches"] = [match]
    data = {"data": [labeled]}

    content = requests.post(
        f"{host}/finetune",
        headers={
            "Content-Type": "application/json",
        },
        data=json.dumps(data),
    ).json()
    doc = content["data"]["docs"][0]
    return doc


def match_score(match):
    return 1 - match["scores"]["cosine"]["value"]


host = "http://localhost:8020"

st.title("Neural Search over Start-Ups Based on Keywords")

query = st.text_area("Type your query, e.g. area of start-up in question or your own specialization, below")

if st.button(label="Search") or query:
    if query:
        doc = search(query, host)

        max_score = max(match_score(match) for match in doc["matches"])

        for match in doc["matches"]:
            id = match["id"]
            score = match_score(match)
            tags = match["tags"]

            name, description = tags["name"], tags["description"]

            st.header(name)
            st.caption(description)

            col1, col2, col3 = st.columns([3, 1, 1])
            with st.container():
                st.markdown("""---""")
                score_diff = score - max_score
                with col1:
                    st.metric("Similarity (100% is the best)", score*100, score_diff*100)
                with col2:
                    if st.button("✔️ Mark as relevant", id):
                        with st.spinner("Finetuning..."):
                            finetune(doc, match, True, host)
                        st.success("Finetuned!")
                        st.experimental_rerun()

                with col3:
                    if st.button("✖️ Mark as irrelevant", id):
                        with st.spinner("Finetuning..."):
                            finetune(doc, match, False, host)
                        st.success("Finetuned!")
                        st.experimental_rerun()
    else:
        st.markdown("Please enter a query")
