# Academic Paper Search - Web Research Skill

## Skill Purpose

Search academic literature sources on the web, retrieve abstracts and metadata, rank by relevance, and optionally download publicly available PDFs for literature review integration.

## When to Use This Skill

- User requests "find recent papers on [topic]"
- User asks to "search literature about [concept]"
- User needs "related work on [technology/method]"
- User wants to update bibliography with current sources
- User mentions specific venues: "papers from IEEE on X" or "arXiv papers about Y"

## Core Capabilities

1. **Multi-source academic search** across Google Scholar, arXiv, Semantic Scholar, IEEE Xplore, Web of Science, Scopus, Mendeley
2. **Abstract extraction** with metadata (title, authors, year, venue, DOI/URL)
3. **Relevance ranking** (0-100 scale) based on user-provided context
4. **PDF extraction** and storage in `papers/` directory
5. **Context-aware matching** using uploaded PDFs, LaTeX files, markdown notes, or chat text

## Workflow Steps

### Phase 1: Context Building (MANDATORY)

Before searching, **always** build a context profile from available sources:

#### 1.1 Identify User Context Sources
```
Check for:
- Uploaded PDF papers (papers/ directory)
- Current LaTeX project (.tex files in project/)
- Markdown notes or summaries (references-new/, *.md)
- Pasted text in chat (extract key terms)
- User-provided keywords (explicit request)
```

#### 1.2 Extract Context Keywords & Concepts
Use `grep_search` and `read_file` to extract:
- **Technical terms**: algorithms, methods, frameworks mentioned
- **Domain keywords**: application area, problem domain
- **Acronyms**: ML, NLP, IoT, etc.
- **Research questions**: stated objectives or hypotheses
- **Cited authors/papers**: existing bibliography as baseline

Example context extraction:
```
Context from project/capitulo2/capitulo2.tex:
- Domain: "sistemas de recomendação", "filtragem colaborativa"
- Methods: "deep learning", "redes neurais"
- Evaluation: "precision", "recall", "F1-score"
- Gap: "falta de interpretabilidade"
```

#### 1.3 Build Search Query Profile
Create structured search intent:
```json
{
  "primary_keywords": ["recommender systems", "collaborative filtering"],
  "secondary_keywords": ["deep learning", "neural networks", "explainability"],
  "exclusions": ["healthcare", "genomics"],  // if context indicates focus
  "time_range": "2020-2025",  // recent = last 5 years unless specified
  "preferred_venues": ["RecSys", "SIGIR", "WWW"]  // extract from context if available
}
```

---

### Phase 2: Multi-Source Search

Execute parallel searches across academic sources using `fetch_webpage`:

#### 2.1 Google Scholar Search
```
URL: https://scholar.google.com/scholar?q={query}&as_ylo={year_start}
Query construction: "{primary_keywords[0]} {primary_keywords[1]} {secondary_keywords[0]}"
Extract: title, authors, year, snippet (abstract preview), citation count, PDF link
```

#### 2.2 arXiv Search
```
URL: https://arxiv.org/search/?query={query}&searchtype=all&order=-submitted_date
Query: Use LaTeX-friendly terms, add category filter (cs.AI, cs.LG, etc.)
Extract: arXiv ID, title, authors, abstract (full), submission date, PDF link
Advantage: Full abstracts available, open access
```

#### 2.3 Semantic Scholar
```
URL: https://www.semanticscholar.org/search?q={query}&sort=relevance
Query: Natural language or keyword-based
Extract: title, authors, year, abstract, citations, "influential citations", venue, DOI
Advantage: Citation context and influence metrics
```

#### 2.4 IEEE Xplore
```
URL: https://ieeexplore.ieee.org/search/searchresult.jsp?queryText={query}
Query: Technical terms, add filters for conference/journal if needed
Extract: title, authors, publication year, abstract, DOI, venue, PDF availability
Note: Full-text access may require institutional login
```

#### 2.5 Additional Sources (Use as Needed)
- **Scopus**: Broad coverage, strong citation metrics
- **Web of Science**: High-impact journals, citation tracking
- **Mendeley**: Community-tagged papers, related recommendations
- **DBLP**: Computer science bibliography (metadata only, redirect to source)

#### 2.6 Fetch Tool Usage Pattern
```
fetch_webpage(
  urls=[
    "https://scholar.google.com/scholar?q=...",
    "https://arxiv.org/search/?query=...",
    "https://www.semanticscholar.org/search?q=..."
  ],
  query="Extract paper titles, authors, abstracts, and links related to {user_topic}"
)
```

**CRITICAL**: Include in `query` parameter: "Focus on extracting title, authors, publication year, abstract text, and PDF/DOI links for papers matching {keywords}."

---

### Phase 3: Abstract & Metadata Extraction

For each source, structure results as:

```markdown
### [Paper Title](DOI_or_URL)
**Authors**: First Author, Second Author, et al.  
**Venue**: Conference/Journal Name, Year  
**Citations**: [if available]  
**Relevance**: [to be calculated in Phase 4]

**Abstract**:
[Full abstract text extracted from source]

**PDF**: [link if available] or "Not publicly available"
```

#### Handling Partial Results
- If abstract not on search results page → fetch individual paper page
- If behind paywall → note "Institutional access required"
- If only snippet available → use snippet + note "Partial abstract"

---

### Phase 4: Relevance Ranking (0-100 Scale)

Compute relevance score for each paper using weighted criteria:

#### Scoring Dimensions

1. **Keyword Match (30 points)**
   - Primary keywords in title: +15 per keyword
   - Primary keywords in abstract: +5 per keyword
   - Secondary keywords in abstract: +2 per keyword
   - Exact phrase match: +10 bonus

2. **Conceptual Alignment (25 points)**
   - Addresses same research gap: +15
   - Uses similar methodology: +10
   - Same application domain: +10
   - Overlapping evaluation metrics: +5

3. **Recency (15 points)**
   - 2024-2025: +15
   - 2022-2023: +12
   - 2020-2021: +8
   - 2018-2019: +4
   - Pre-2018: +0

4. **Citation Impact (15 points)**
   - >100 citations: +15
   - 50-100: +12
   - 20-49: +8
   - 10-19: +5
   - <10: +2
   - Not available: +5 (neutral)

5. **Venue Quality (10 points)**
   - A* venue (CORE ranking): +10
   - A venue: +8
   - B venue: +5
   - Workshop/preprint: +3

6. **User Context Fit (5 points)**
   - Cites papers from user's bibliography: +5
   - Author overlap with user's citations: +3
   - Uses same dataset/benchmark: +4

#### Normalization
```
final_score = min(100, sum_of_dimensions)
```

#### Presentation
Sort results by relevance score (descending) and display:
```
**Relevance: 87/100** ⭐⭐⭐⭐⭐ (Highly Relevant)
**Relevance: 68/100** ⭐⭐⭐⭐ (Relevant)
**Relevance: 45/100** ⭐⭐⭐ (Moderately Relevant)
**Relevance: 22/100** ⭐⭐ (Tangentially Relevant)
```

---

### Phase 5: PDF Extraction (On Request Only)

When user explicitly requests "download PDFs" or "extract papers to papers/ folder":

#### 5.1 Create Python Download Script
```python
# tools/download_papers.py
import requests
import os
from pathlib import Path

def download_pdf(url, filename, dest_folder="papers"):
    """Download PDF from public URL and save to papers/ folder"""
    Path(dest_folder).mkdir(exist_ok=True)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Academic Research Tool)'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 200 and 'application/pdf' in response.headers.get('Content-Type', ''):
            filepath = os.path.join(dest_folder, filename)
            with open(filepath, 'wb') as f:
                f.write(response.content)
            return True, filepath
        else:
            return False, f"Not a valid PDF (status: {response.status_code})"
    except Exception as e:
        return False, str(e)

# Example usage
papers_to_download = [
    ("https://arxiv.org/pdf/2301.12345.pdf", "smith2023_recommender.pdf"),
    ("https://example.com/paper.pdf", "jones2024_neural.pdf"),
]

for url, filename in papers_to_download:
    success, result = download_pdf(url, filename)
    if success:
        print(f"✓ Downloaded: {result}")
    else:
        print(f"✗ Failed {filename}: {result}")
```

#### 5.2 Invoke Download Tool
```
run_in_terminal(
  command="cd /path/to/workspace && python tools/download_papers.py",
  explanation="Downloading publicly available PDFs to papers/ folder",
  isBackground=False
)
```

#### 5.3 Handle Download Failures
- **403/401**: Note "Requires institutional access, provide DOI instead"
- **404**: "Link broken, check publisher's website"
- **Paywalled**: Suggest user manually download via institution or use DOI

#### 5.4 Post-Download Actions
After successful downloads, suggest:
```
✓ PDFs saved to papers/
Next steps:
- Run `python tools/extract_papers.py` to extract abstracts
- Run `python tools/review_papers.py` for deep section analysis
- Add BibTeX entries to references.bib using DOI
```

---

## Output Format Examples

### Search Results Presentation

```markdown
## Literature Search Results: "Explainable Recommender Systems"

**Context**: Based on your project/capitulo2/capitulo2.tex focusing on collaborative filtering with deep learning and interpretability gap.

**Search Query**: "explainable recommender systems deep learning interpretability 2020-2025"

**Sources Searched**: Google Scholar, arXiv, Semantic Scholar, IEEE Xplore

---

### 🥇 [Attention-Based Explanations for Collaborative Filtering](https://doi.org/10.1145/3383313.3412345)

**Relevance: 92/100** ⭐⭐⭐⭐⭐ (Highly Relevant)

**Authors**: Maria Silva, John Smith, Ana Costa  
**Venue**: RecSys 2023 (ACM Conference on Recommender Systems)  
**Citations**: 47  
**PDF**: [arXiv preprint](https://arxiv.org/pdf/2301.12345.pdf)

**Abstract**:
We propose an attention-based neural collaborative filtering model that provides post-hoc explanations for recommendations. Our approach uses multi-head attention to identify which user-item interactions most influenced each prediction, generating natural language explanations. Experiments on MovieLens-1M and Amazon datasets show NDCG@10 improvements of 4.2% over baseline NCF while achieving 78% explanation quality (user study). The model addresses the interpretability gap in deep learning recommender systems...

**Relevance Breakdown**:
- Keyword Match: 28/30 (all primary keywords in title/abstract)
- Conceptual Alignment: 25/25 (addresses interpretability gap directly)
- Recency: 15/15 (2023)
- Citation Impact: 9/15 (47 citations)
- Venue Quality: 10/10 (RecSys is A* venue)
- Context Fit: 5/5 (cites Zhang et al. from your bibliography)

---

### 🥈 [Neural Collaborative Filtering with Interpretable Components](https://arxiv.org/abs/2312.98765)

**Relevance: 85/100** ⭐⭐⭐⭐⭐ (Highly Relevant)

**Authors**: David Lee, Sophie Turner  
**Venue**: arXiv preprint, 2024  
**Citations**: 12  
**PDF**: [arXiv](https://arxiv.org/pdf/2312.98765.pdf)

**Abstract**:
This paper introduces InterNCF, a neural collaborative filtering architecture with built-in interpretability. Unlike post-hoc explanation methods, our model learns disentangled representations for different preference dimensions (genre, style, quality) using variational autoencoders. Evaluation on three public datasets demonstrates competitive accuracy (RMSE=0.82 on MovieLens-10M) while providing fine-grained explanations...

[... continue for 5-10 most relevant papers ...]

---

**Summary**:
- Found **23 papers** matching criteria (showing top 10 by relevance)
- Average relevance: 68/100
- 5 papers with direct interpretability focus (>80 relevance)
- 8 papers from 2023-2024 (recent)
- 3 PDFs publicly available for download

**Recommendation**: Start with Silva et al. (2023) and Lee & Turner (2024) for Chapter 3 (Trabalhos Relacionados). Would you like me to:
1. Download the publicly available PDFs?
2. Generate BibTeX entries for these papers?
3. Search for more papers on a specific subtopic?
```

---

## Tool Integration Checklist

### Required Tools
- ✅ `fetch_webpage`: Multi-source search execution
- ✅ `read_file`: Extract context from user's LaTeX/MD files
- ✅ `grep_search`: Find keywords across project files
- ✅ `run_in_terminal`: Execute Python PDF download script
- ✅ `create_file`: Generate download_papers.py if not exists

### Validation Steps
1. **Pre-search**: Confirm context keywords extracted (show to user)
2. **Post-search**: Show number of results per source
3. **Post-ranking**: Display score distribution histogram
4. **Post-download**: Verify PDF file sizes and readable PDFs

---

## Common User Requests & Responses

### "Find papers on [topic]"
1. Extract topic keywords
2. Check project/ files for additional context
3. Search 3-4 main sources (Scholar, arXiv, Semantic Scholar)
4. Return top 10 ranked results

### "Recent work on [topic]"
- Add time filter: last 2-3 years
- Prioritize preprints (arXiv) and latest conference proceedings
- Boost recency score weight to 25 points

### "Papers from [venue]"
- Add venue filter to search queries
- Focus on IEEE Xplore (for IEEE), ACM DL (for ACM), specific conference sites
- Note conference year range

### "Download PDFs for top 5 papers"
- Filter for public PDFs only (arXiv, open access journals)
- Generate download script with those 5 URLs
- Execute and report success/failure per paper

### "Papers similar to [uploaded_pdf]"
- Extract title, abstract, keywords from uploaded PDF (use `tools/extract_papers.py`)
- Use extracted content as primary context
- Weight "Conceptual Alignment" dimension higher (35 points)

---

## Error Handling & Edge Cases

### No Results Found
```
No papers found matching "{query}" in initial search.

Suggestions:
- Broaden keywords (remove very specific terms)
- Try alternative terminology (e.g., "neural networks" → "deep learning")
- Extend time range (include pre-2020)
- Check spelling of technical terms

Would you like me to try a broader search?
```

### Source Unavailable (fetch fails)
- Skip that source, continue with others
- Note in output: "⚠️ IEEE Xplore unreachable, searched 3/4 sources"

### All PDFs Behind Paywall
```
⚠️ No publicly available PDFs found for top results.

Alternatives:
- Provided DOI links for institutional access
- Check if preprints exist on arXiv/ResearchGate
- Search authors' personal websites
- Request via interlibrary loan

DOI links provided for all papers.
```

### Ambiguous Context
If user provides no context and minimal keywords:
```
⚠️ Limited context detected. To improve relevance ranking, please provide:
- Your research focus (paste abstract or keywords)
- Specific methods you're using
- Application domain
- Or upload a reference paper

Proceeding with keyword-only search for now...
```

---

## Integration with Existing Workflows

### After Search → Update Bibliography
```
Suggest next step: "Add these papers to references.bib?"
If yes, invoke bibtex-reference-management skill to:
- Generate BibTeX entries from DOIs
- Add to project/references.bib
- Validate format and keys
```

### After PDF Download → Extract Content
```
Suggest: "Run extraction tools on downloaded PDFs?"
If yes:
- python tools/extract_papers.py (titles + abstracts)
- python tools/review_papers.py (methodology + results)
- Create summaries in references-new/
```

### For TCC Chapter 3 (Trabalhos Relacionados)
```
Offer: "Generate comparative table draft for Chapter 3?"
If yes:
- Use top 5-7 papers
- Extract key features/contributions
- Format as LaTeX table with \ticV/\ticX markers
- Insert in capitulo3/capitulo3.tex
```

---

## Success Criteria

A successful search session includes:
- ✅ Context extracted from ≥2 sources (user files + explicit keywords)
- ✅ ≥3 academic sources searched
- ✅ ≥5 relevant papers found (relevance >60)
- ✅ Full abstracts retrieved for top results
- ✅ Relevance scores calculated and explained
- ✅ Links provided (DOI or direct URLs)
- ✅ PDF availability clearly indicated
- ✅ (If requested) PDFs downloaded successfully to papers/

---

## Advanced Features (Optional Extensions)

### Citation Network Exploration
- From top paper, find "cited by" papers (forward citations)
- Find "references" from top paper (backward citations)
- Build citation graph to discover seminal works

### Author Tracking
- Identify prolific authors in search results
- Suggest "other papers by [Author]" searches
- Build co-authorship network

### Temporal Trend Analysis
- Group results by year
- Show publication frequency over time
- Identify emerging vs established topics

### Venue Analysis
- Rank by venue prestige
- Suggest target venues for user's work based on related work venues
- Note acceptance rates if available

---

## Skill Activation Phrases

This skill should trigger on:
- "search for papers on..."
- "find literature about..."
- "recent work in [field]"
- "related papers to [topic]"
- "academic sources on..."
- "arxiv papers about..."
- "what's the state of the art in..."
- "find [N] papers on [topic]"
- "search Google Scholar for..."

---

## Final Checklist Before Returning Results

- [ ] Context summary shown to user (transparency)
- [ ] All search queries executed
- [ ] Abstracts extracted (not just titles)
- [ ] Relevance scores calculated with breakdown
- [ ] Results sorted by relevance
- [ ] Links verified (no broken URLs)
- [ ] PDF availability indicated
- [ ] Next steps suggested (download, add to bib, extract)
- [ ] Total papers found count reported
- [ ] Sources searched list provided

---

## Example Complete Interaction

**User**: "Find recent papers on federated learning for IoT"

**Agent**:
1. *Reads project/capitulo1/capitulo1.tex and project/capitulo2/capitulo2.tex*
2. "I found your project focuses on edge computing and privacy-preserving ML. I'll search for federated learning papers with IoT context, prioritizing edge deployment and privacy aspects."
3. *Searches Google Scholar, arXiv, Semantic Scholar, IEEE Xplore*
4. *Extracts 18 papers, ranks by relevance*
5. *Presents top 10 with full abstracts, scores, and links*
6. "Found 18 papers (2020-2025), showing top 10. 6 papers have public PDFs available. Would you like me to download the top 5 PDFs and add BibTeX entries to references.bib?"

**User**: "Yes, download and add to bibliography"

**Agent**:
1. *Creates/updates tools/download_papers.py*
2. *Runs download script, 4/5 successful*
3. *Invokes bibtex-reference-management skill*
4. *Adds 5 BibTeX entries to references.bib*
5. "✓ Done! 4 PDFs in papers/, 5 entries in references.bib. Run check_cites.py to validate?"

---

## Notes

- **Respect rate limits**: Space out fetch requests by 2-3 seconds if making many calls
- **Cache results**: Store search results temporarily to avoid re-fetching
- **User feedback**: Ask if results match expectations; refine query if needed
- **Ethical scraping**: Use academic search APIs when available; respect robots.txt
- **Citation format**: Prefer DOI over direct URLs for permanence

