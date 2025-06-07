import requests

def generate_report(summary: str, corrections: str) -> str:
    prompt = f"""Using the summary and fact check comments below, write a fine
Summary:\n{summary}
Corrections:\n{corrections}
Compile the corrected insights into a clean, cohesive, and structured report. Maintain a neutral, analytical tone suitable for industry stakeholders or policymakers. The report must reflect only accurate, verified, and strategically useful content derived from the corrected summary. Ensure clarity, precision, and decision-making utility.
Note: use Font Bold for highlight important words and headings and add content where ever you can in good format with proper spacing. Provide a .doc file at last.
(Important Constraints:

Do not include hallucinated or speculative content.

Do not fabricate facts or invent metrics.

Do not drift into unrelated domains or global examples unless directly relevant.

Do not summarize based on your own knowledge; rely solely on search output.

Ensure logical flow, factual accuracy, and structured formatting.

Note: use Font Bold for highlight important words and headings and add content where ever you can.) - No need this information in output

"""
    response = requests.post("http://localhost:11434/api/generate",
                             json= {
                                 "model":"llama2",
                                 "prompt":prompt,
                                 "stream":False
                             })
    return response.json()["response"].strip()