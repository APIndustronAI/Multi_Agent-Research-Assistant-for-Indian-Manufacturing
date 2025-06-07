import requests

def summarize_text(text:str)->str:
    prompt = f"""From the gathered search data, generate a concise, high-fidelity summary. Each bullet point must convey a core insight or fact that directly addresses the original topic. Do not include generalizations, filler content, or unrelated global information unless it provides a meaningful comparison with India’s manufacturing context:\n\n{text}
    (Important Constraints:

Do not include hallucinated or speculative content.

Do not fabricate facts or invent metrics.

Do not drift into unrelated domains or global examples unless directly relevant.

Do not summarize based on your own knowledge; rely solely on search output.

Ensure logical flow, factual accuracy, and structured formatting.

Note: use Font Bold for highlight important words and headings and add content where ever you can.) - No need this information in output"""
    response = requests.post("http://localhost:11434/api/generate", 
                             json = {
                                 "model": "llama2",
                                 "prompt": prompt,
                                 "stream": False })
    return response.json()["response"].strip()