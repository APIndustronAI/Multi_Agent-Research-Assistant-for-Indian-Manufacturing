import requests

def fact_check(text: str) -> str:
    prompt = f"""Check this summary for bias or hallucination. Cross-check every statement using credible references. Remove or revise any claim that lacks strong supporting evidence. Ensure all remaining insights are backed by verified data and remain relevant to Indian manufacturing. Clearly specify changes made, referencing the correction source.:\n\n{text}
    (Important Constraints:

Do not include hallucinated or speculative content.

Do not fabricate facts or invent metrics.

Do not drift into unrelated domains or global examples unless directly relevant.

Do not summarize based on your own knowledge; rely solely on search output.

Ensure logical flow, factual accuracy, and structured formatting.

Note: use Font Bold for highlight important words and headings and add content where ever you can.) - No need this information in output
    """
    response = requests.post("http://localhost:11434/api/generate",
                            json={"model": "llama2", "prompt": prompt, "stream": False})
    return response.json()["response"].strip()