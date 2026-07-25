import csv
import time
from google_play_scraper import reviews, Sort

# ID aplikasi DANA di Play Store
APP_ID = "id.dana"
LANG = "id"
COUNTRY = "id"

# Target total: sekitar 500-1000 data (negatif + positif digabung)
# (negatif = bintang 1 & 2, positif = bintang 4 & 5)
# 250 per bintang -> 500 negatif + 500 positif = 1000 total
TARGET_PER_SCORE = 250
BATCH = 200              # jumlah review per permintaan


def fetch_by_score(score, target):
    """Mengambil review dengan rating tertentu hingga mencapai target."""
    collected = []
    continuation = None
    while len(collected) < target:
        try:
            if continuation is None:
                result, continuation = reviews(
                    APP_ID,
                    lang=LANG,
                    country=COUNTRY,
                    sort=Sort.NEWEST,
                    count=BATCH,
                    filter_score_with=score,
                )
            else:
                result, continuation = reviews(
                    APP_ID,
                    lang=LANG,
                    country=COUNTRY,
                    sort=Sort.NEWEST,
                    count=BATCH,
                    filter_score_with=score,
                    continuation_token=continuation,
                )
        except Exception as e:
            print(f"  ⚠ Gagal mengambil review bintang {score}: {e}")
            break
        if not result:
            print(f"  ℹ Tidak ada review bintang {score} lagi (total {len(collected)}).")
            break
        collected.extend(result)
        print(f"  ↳ bintang {score}: {len(collected)} terkumpul")
        if continuation is None:
            break
        time.sleep(1)  # jeda agar tidak membebani server
    return collected[:target]


def to_rows(items, sentiment):
    rows = []
    for r in items:
        rows.append({
            "rating": r.get("score"),
            "review": (r.get("content") or "").replace("\n", " ").strip(),
            "tanggal": str(r.get("at")) if r.get("at") else "",
            "author": r.get("author") or "",
            "thumbs_up": r.get("thumbsUpCount") or 0,
            "sentimen": sentiment,
        })
    return rows


def save_csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["rating", "review", "tanggal", "author", "thumbs_up", "sentimen"]
        )
        writer.writeheader()
        writer.writerows(rows)


def main():
    print("=" * 60)
    print("SCRAPING REVIEW APLIKASI DANA DARI GOOGLE PLAY STORE")
    print("=" * 60)

    # --- Review Negatif (bintang 1 & 2) ---
    print("\n[1/2] Mengambil review NEGATIF (bintang 1 & 2)...")
    neg_1 = fetch_by_score(1, TARGET_PER_SCORE)
    neg_2 = fetch_by_score(2, TARGET_PER_SCORE)
    neg_rows = to_rows(neg_1, "Negatif") + to_rows(neg_2, "Negatif")
    print(f"  ✅ Total review negatif: {len(neg_rows)}")

    # --- Review Positif (bintang 4 & 5) ---
    print("\n[2/2] Mengambil review POSITIF (bintang 4 & 5)...")
    pos_4 = fetch_by_score(4, TARGET_PER_SCORE)
    pos_5 = fetch_by_score(5, TARGET_PER_SCORE)
    pos_rows = to_rows(pos_4, "Positif") + to_rows(pos_5, "Positif")
    print(f"  ✅ Total review positif: {len(pos_rows)}")

    # --- Simpan file ---
    save_csv("Scraping/dana_reviews_negatif.csv", neg_rows)
    save_csv("Scraping/dana_reviews_positif.csv", pos_rows)
    save_csv("Scraping/dana_reviews_semua.csv", neg_rows + pos_rows)

    print("\n" + "=" * 60)
    print("🎉 SELESAI! File hasil scraping:")
    print(f"   - Scraping/dana_reviews_negatif.csv ({len(neg_rows)} data)")
    print(f"   - Scraping/dana_reviews_positif.csv ({len(pos_rows)} data)")
    print(f"   - Scraping/dana_reviews_semua.csv   ({len(neg_rows) + len(pos_rows)} data)")
    print("=" * 60)


if __name__ == "__main__":
    main()