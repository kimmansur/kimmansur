"""Galaxy header where each star is one of the systems (code private), grouped by theme as arms.
Uses galaxy-profile's renderer (GPL-3.0) with a hand-made snapshot instead of the GitHub API."""
import json, sys
from datetime import date
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import yaml
from generator import build, data
from generator.config import validate_config

# (slug, created, weight, theme) — weight drives brightness only
SYSTEMS = [
 ("SUS billing","2025-07-01",40,0), ("procedure-table","2025-08-01",20,0),
 ("waiting lists","2025-06-01",40,1), ("network-panels","2025-09-01",15,1),
 ("provider accountability","2025-08-15",30,2), ("nonprofit-partnerships","2026-03-01",10,2),
 ("procurement","2026-01-15",20,2), ("price-research","2026-02-01",8,2),
 ("process tracker","2025-10-01",30,3), ("residency-portal","2025-11-01",20,3),
 ("events","2025-12-01",8,3), ("medicine-stock","2026-04-01",5,3), ("invoices","2026-05-01",10,3),
]
TODAY = date.today()

def snapshot():
    nodes = [{"name": s, "nameWithOwner": f"kimmansur/{s}", "isFork": False, "stargazerCount": w,
              "createdAt": f"{c}T12:00:00Z", "pushedAt": f"{TODAY.isoformat()}T12:00:00Z",
              "description": "", "primaryLanguage": {"name": "Python"},
              "languages": {"totalSize": 1, "edges": [{"size": 1, "node": {"name": "Python"}}]},
              "repositoryTopics": {"nodes": []}} for s, c, w, _ in SYSTEMS]
    weeks = [{"contributionDays": [{"date": TODAY.isoformat(), "contributionCount": 0}]}]
    payload = {"data": {"user": {"login": "kimmansur", "pullRequests": {"totalCount": 0}, "issues": {"totalCount": 0},
               "contributionsCollection": {"contributionCalendar": {"totalContributions": 0, "weeks": weeks}},
               "repositories": {"totalCount": len(nodes), "nodes": nodes}}}}
    return data.from_graphql(payload, TODAY)

def main():
    raw = yaml.safe_load((ROOT / "config.yml").read_text(encoding="utf-8"))
    themes = [a["name"] for a in raw["galaxy_arms"]]
    for i, arm in enumerate(raw["galaxy_arms"]):
        arm["repos"] = [s for s, _, _, t in SYSTEMS if t == i]
    raw["projects"] = [{"repo": f"kimmansur/{n}", "description": n, "arm": t} for n, t in (("SUS billing",0),("waiting lists",1),("provider accountability",2),("process tracker",3))]
    config = validate_config(raw)
    files = build.render_all(config, snapshot())
    out = ROOT / "assets" / "generated"; out.mkdir(parents=True, exist_ok=True)
    for name, svg in files.items():
        if name.startswith("galaxy-header"):
            (out / name).write_text(svg, encoding="utf-8")
    print("galaxy header written; arms:", themes)

if __name__ == "__main__":
    main()
