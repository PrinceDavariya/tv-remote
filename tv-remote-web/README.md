# Android TV Remote (Vercel + Local Bridge)

This setup lets you host a web UI on Vercel while sending commands to your Android TV through a local bridge that you run only when needed.

## 1) Local Bridge (run when needed)

Requirements:
- ADB installed on your PC
- Android TV on same Wi-Fi
- Developer Options + Wireless Debugging enabled

Steps:
1. Connect ADB once:
   - `adb connect <TV_IP>:5555`
2. Install Python deps:
   - `pip install -r tv-remote-bridge/requirements.txt`
3. Start the bridge (only when you need it):
   - `set TV_HOST=<TV_IP>:5555`
   - `python tv-remote-bridge/bridge.py`

Bridge runs on: `http://<PC_IP>:8787`

## 2) Vercel Frontend

Deploy the folder `tv-remote-web` to Vercel (static site).

In the UI:
- Set Bridge URL to `http://<PC_IP>:8787` if you're on home Wi-Fi
- If you want to access from anywhere, put the bridge behind Tailscale or Cloudflare Tunnel and use that URL

## Notes
- The bridge must be running to send commands.
- If you change networks or IPs, update the Bridge URL in the web UI.
