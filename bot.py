import asyncio
from playwright.async_api import async_playwright
from datetime import datetime
import os
from datetime import datetime

# THIS IS THE MAGIC LINE: It finds the folder where THIS bot.py lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "warehouse_data.csv")

print(f"📍 DEBUG: The bot is officially writing to: {DATA_FILE}")

# --- CONFIGURATION ---
# --- NEW STABLE CONFIGURATION ---
TARGET_URL = "https://www.scrapethissite.com/pages/forms/"
SELECTOR = ".os-stats" # This picks the first 'Oscar Winning' team's stats
INTERNAL_PORTAL_URL = "https://demo.playwright.dev/todomvc/#/"
async def run_automation():
    async with async_playwright() as p:
        print(f"--- 🏁 Session Started: {datetime.now().strftime('%H:%M:%S')} ---")
        
        # Launching with a specific window size to ensure the layout is consistent
        browser = await p.chromium.launch(headless=False) 
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        processed_value = 0
        status = "Initialization"

        try:
            print(f"📡 Step 1: Navigating to Stable Source...")
            await page.goto(TARGET_URL, wait_until="load")
            
            # --- MULTI-TEAM EXTRACTION LOOP ---
            print(f"🔍 Step 2: Extracting Top 5 Teams...")
            
            # Get the lists of names and wins
            names = await page.locator(".name").all_inner_texts()
            wins = await page.locator(".wins").all_inner_texts()

            # We loop through the first 5 to keep the dashboard clean
            for i in range(5):
                team_name = names[i].strip()
                wins_count = float(wins[i].strip())
                
                # Create a unique metric name for each team
                metric_name = f"Wins_{team_name.replace(' ', '_')}"
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                
                # Log each team as a separate line in the CSV
                log_entry = f"{timestamp},{metric_name},{wins_count},Success\n"
                
                with open(DATA_FILE, "a+", encoding="utf-8") as f:
                    f.write(log_entry)
                
                print(f"✅ Captured: {team_name} ({wins_count} wins)")

            status = "Success" # Mark the overall run as successful

        except Exception as e:
            status = f"Loop Error: {str(e)[:20]}" 
            print(f"❌ {status}")

            print("📜 Step 2: Scrolling to render dynamic content...")
            await page.mouse.wheel(0, 800)
            await asyncio.sleep(3) 
            
            # --- SMART EXTRACTION ---
            print(f"🔍 Step 4: Extracting price with European format support...")
            # This locator finds the price span regardless of the currency symbol
            price_element = page.locator(".s-item__price").first
            
            if await price_element.count() > 0:
                raw_value = await price_element.inner_text()
                print(f"📍 Raw Data Found: {raw_value}")
                
                # Cleaning Logic for "EUR 1.080,82" or "$1,599.00"
                # We remove non-numeric chars except for the decimal separator
                clean_string = raw_value.replace("EUR", "").replace("$", "").replace(" ", "")
                # If it uses European formatting (1.080,82), we swap , for .
                if "," in clean_string and "." in clean_string:
                    clean_string = clean_string.replace(".", "").replace(",", ".")
                elif "," in clean_string:
                    clean_string = clean_string.replace(",", ".")

                processed_value = float("".join(c for c in clean_string if c.isdigit() or c == "."))
                status = "Success"
            else:
                status = "Selector Timeout"
                print("⚠️ Warning: Price element still not visible.")
        except Exception as e:
            status = f"System Error: {str(e)[:20]}" 
            print(f"❌ {status}")

        # --- PHASE 2: DATA ENTRY (The Goal) ---
        if status == "Success":
            print(f"🚀 Step 5: Updating Internal System with ${processed_value}...")
            try:
                await page.goto(INTERNAL_PORTAL_URL)
                await page.fill(".new-todo", f"Automated Update: RTX 5090 is ${processed_value}")
                await page.keyboard.press("Enter")
                await asyncio.sleep(2)
            except:
                print("⚠️ Internal Portal unreachable.")

        # --- PHASE 3: FORCED LOGGING (The Fix for your CSV) ---
        print("💾 Step 6: Committing to Warehouse...")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        log_entry = f"{timestamp},Market_Price_RTX5090,{processed_value},{status}\n"
        
        # We use 'a+' (append and read) and force a flush to disk
        file_exists = os.path.exists(DATA_FILE)
        with open(DATA_FILE, "a+", encoding="utf-8") as f:
            if not file_exists or os.stat(DATA_FILE).st_size == 0:
                f.write("Timestamp,Metric_Name,Value,Execution_Status\n")
            f.write(log_entry)
            f.flush() # Forces the Mac to save the file immediately
            os.fsync(f.fileno()) # Double-force save to hardware

        await browser.close()
        print(f"--- 🏁 Session Closed Status: {status} ---\n")

if __name__ == "__main__":
    asyncio.run(run_automation())