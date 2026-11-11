# Roblox Banner & PFP Maker
Static three.js app. The map (Crossroads.rbxl) is pre-converted to `public/scene.json` by `convert.py`.

**Deploy to Render:** push this folder to a Git repo, then New + > Blueprint (uses `render.yaml`), or New + > Static Site with build command `npm install && npm run build` and publish directory `public`.

**Run locally:** `npm install && npm run dev`

**Different map/spawn:** `python3 convert.py YourPlace.rbxl public/scene.json` (XML .rbxl only; spawn points become the location dropdown).

**Character:** your RobloxNoobRig model, converted from `RobloxNoobRig.proj` to `public/noob.json` (+ `public/NoobTexture.png`) by `convert_noob.py`. Poses are defined in the `POSES` table in `public/index.html`.
