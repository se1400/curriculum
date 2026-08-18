#!/bin/bash
# Prints everything about a slide deck that MUST be preserved before it's
# restyled: its own CSS variable names, which of those variables JS reads
# dynamically, every id/class/dataset key JS depends on, whether it uses the
# standard showSlide/changeSlide engine, and any live CSS-custom-property
# demos that need individual care rather than a generic palette swap.
#
# Usage: scripts/inventory_slide.sh slides/some-deck.html

set -u
# Deliberately no -e/pipefail: every section below is best-effort — a section
# with zero matches (e.g. a deck with no <iframe>) is informative, not an error,
# and the script should keep going and report everything it can.

FILE="$1"
if [ ! -f "$FILE" ]; then
  echo "File not found: $FILE" >&2
  exit 1
fi

echo "=== $FILE ==="
echo

echo "--- :root custom properties (name: value) ---"
awk '/:root *\{/{f=1} f{print} /\}/{if(f){exit}}' "$FILE" | grep -E '^\s*--' || echo "(none found — check for a different token pattern)"
echo

echo "--- variables referenced inside <script> (these MUST keep their exact name) ---"
awk '/<script>/{f=1} /<\/script>/{f=0} f' "$FILE" | grep -oE -- '--[a-zA-Z0-9-]+' | sort -u || echo "(none — this deck's script doesn't reference CSS variables directly)"
echo

echo "--- ids / classes / dataset keys the script depends on (do not rename) ---"
awk '/<script>/{f=1} /<\/script>/{f=0} f' "$FILE" | grep -noE "getElementById\('[^']+'\)|querySelector\('[^']+'\)|querySelectorAll\('[^']+'\)|classList\.(add|remove|toggle|contains)\('[^']+'\)|\.dataset\.[a-zA-Z]+" | sort -u -t: -k2 || echo "(none found)"
echo

echo "--- onclick-invoked function names (do not rename without updating every call site) ---"
grep -noE "onclick=\"[a-zA-Z0-9_]+\(" "$FILE" | sed -E "s/onclick=\"//; s/\(//" | sort -u || echo "(none found)"
echo

echo "--- live CSS-custom-property mutation (HIGH RISK — inspect by hand, don't repoint blindly) ---"
grep -n "style.setProperty\|documentElement.style" "$FILE" || echo "(none found)"
echo

echo "--- standard deck-engine check ---"
if grep -q "function showSlide" "$FILE" && grep -q "function changeSlide" "$FILE"; then
  echo "showSlide/changeSlide: present (standard engine)"
else
  echo "showSlide/changeSlide: NOT FOUND — this deck likely uses a different navigation mechanism. Read the whole <script> block before assuming the rail/fit-to-screen scaffold applies."
fi
for id in slide-counter prevBtn nextBtn progress-bar; do
  if grep -q "getElementById('$id')" "$FILE"; then
    echo "#$id: found"
  else
    echo "#$id: NOT FOUND"
  fi
done
echo

echo "--- iframe embeds (CodePen etc. — src URLs must be copied verbatim) ---"
grep -c "<iframe" "$FILE" | xargs -I{} echo "{} iframe(s) found"
grep -oE 'src="[^"]*"' "$FILE" | grep -i codepen || true
echo

echo "--- recurring component classes present in this file ---"
for cls in card two-col ref-table demo-box demo-grid mini-card detail-panel highlight-box highlight note caution qa index-list; do
  count=$(grep -oE "class=\"[^\"]*\b$cls\b[^\"]*\"" "$FILE" | wc -l | tr -d ' ')
  if [ "$count" != "0" ]; then
    echo "$cls: $count occurrence(s)"
  fi
done
