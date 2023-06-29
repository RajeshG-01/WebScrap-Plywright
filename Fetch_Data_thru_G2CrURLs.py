import asyncio
import json
from playwright.async_api import async_playwright

async def scrape_g2crowd_urls(urls):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        page = await browser.new_page()

        scraped_data = []

        try:
            for url in urls:
                await page.goto(url)


                html_content = await page.content()

                scraped_data.append({
                    'URL': url,
                    'HTML': html_content
                })

            return scraped_data

        except asyncio.TimeoutError:
            print("Timeout occurred while scraping the page.")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

        finally:
            await browser.close()

#NOTE: csv_file_path and output_file_path need to change the paths based on requirement

csv_file_path = 'C:/Users/X1 YOGO - 6ND/Desktop/WebScrap-Plywright/URLS.csv'  # Path to your CSV file containing G2Crowd URLs
output_file_path = 'C:/Users/X1 YOGO - 6ND/Desktop/WebScrap-Plywright/Fecthed_JSON_Data.json'  # Path to the output JSON file

urls = []
with open(csv_file_path, 'r') as file:
    for line in file:
        urls.append(line.strip())

loop = asyncio.get_event_loop()
scraped_data = loop.run_until_complete(scrape_g2crowd_urls(urls))

with open(output_file_path, 'w') as file:
    json.dump(scraped_data, file, indent=4)

print("Scraping completed and data saved to", output_file_path)
