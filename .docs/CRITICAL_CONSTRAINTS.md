# CRITICAL CONSTRAINTS - READ THIS FIRST

## ⚠️ Files NOT Synced to GitHub

The following folders are in `.gitignore` and **CANNOT be referenced directly** in any GitHub-pushed code:

```
StudentProjects/
Pitches/
Research/
```

### Why This Matters

These folders contain large files (multi-MB PowerPoints, PDFs, research materials) that cannot be pushed to GitHub.

### What You MUST Do

When working with these files, you have TWO options:

#### Option 1: Move Files (Preferred for website assets)
```bash
# Move the file to a location that WILL be synced
cp StudentProjects/[project]/document.pdf assets/documents/[project]/
# Now you can reference: /assets/documents/[project]/document.pdf
```

#### Option 2: Create Summary (Preferred for large/temporary files)
```bash
# Create a summary in .docs/ (this IS synced)
# Write extracted information to .docs/[project]-summary.md
# Reference the summary, not the original file
```

### ❌ NEVER Do This

```markdown
<!-- WRONG - File won't exist on GitHub -->
[Download Guide](StudentProjects/Cacao track/guide.pdf)

<!-- WRONG - Link will be broken on deployed site -->
documentation:
  url: "/StudentProjects/CRM track/presentation.pptx"
```

### ✅ ALWAYS Do This

```markdown
<!-- CORRECT - File copied to synced location -->
[Download Guide](assets/documents/cacao-guide/guide.pdf)

<!-- CORRECT - Reference to deployed location -->
documentation:
  url: "/assets/documents/cacao-guide/presentation.pdf"
```

---

## 🔄 Workflow for Student Projects

1. **Read** files from `StudentProjects/[track]/` (local only)
2. **Extract** information into summary notes
3. **Copy** important PDFs/presentations to `assets/documents/[project-name]/`
4. **Update** `_projects/[project-name].md` with references to `assets/documents/`
5. **Verify** all links point to `assets/` not `StudentProjects/`

---

## 🔄 Workflow for Pitches

1. **Read** files from `Pitches/` (local only)
2. **Create** summary in `.docs/pitches-analysis.md`
3. **Extract** key information for website narrative
4. **DO NOT** link directly to Pitches folder in any web page
5. **Convert** selected pitch content into website-ready format

---

## 📊 Current Folder Status

| Folder | In Git? | Can Reference? | Usage |
|--------|---------|----------------|-------|
| `StudentProjects/` | ❌ No | ❌ No | Read locally, copy to `assets/documents/` |
| `Pitches/` | ❌ No | ❌ No | Read locally, extract to `.docs/` summaries |
| `Research/` | ❌ No | ❌ No | Read locally, extract insights |
| `assets/documents/` | ✅ Yes | ✅ Yes | Safe to reference in website |
| `.docs/` | ✅ Yes | ✅ Yes | Safe for documentation |
| `_projects/` | ✅ Yes | ✅ Yes | Safe for project pages |

---

## 🚨 If You Forget This

Problems that WILL occur:
- 404 errors on deployed website
- Broken download links
- Missing project documentation
- Jekyll build failures
- Confused users unable to access files

---

## ✅ Pre-Commit Checklist

Before ANY git commit involving student projects or pitches:

- [ ] Are all file references in `_projects/*.md` pointing to `assets/` not `StudentProjects/`?
- [ ] Did I copy necessary PDFs/presentations to `assets/documents/[project]/`?
- [ ] Are all links tested and working?
- [ ] Did I create summaries instead of linking to ignored folders?
- [ ] Can the website run WITHOUT the StudentProjects/Pitches folders?

---

**Remember:** Local files ≠ Deployed files. Always think about what exists on GitHub!

