# Copyright 2025 Seamus.F.Rodrigues
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import requests
import os
import dotenv

dotenv.load_dotenv()

def fetch_jobs(
    location, skills, remote=None, part_time=None, full_time=None,
):
    """
    Fetches job listings from Adzuna based on specified criteria.

    Parameters:
    - location (str): The job location (e.g., 'Pune').
    - skills (str): Skills or keywords to search for (e.g., 'Python, Django').
    - remote (bool, optional): If True, filters for remote jobs.
    - part_time (bool, optional): If True, filters for part-time jobs.
    - full_time (bool, optional): If True, filters for full-time jobs.

    Returns:
    - List[dict]: A list of dictionaries containing job details.
    """

    base_url = os.environ["BASE_URL"]

    APP_ID = os.environ["APP_ID"]
    APP_KEY = os.environ["APP_KEY"]

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what_or": ",".join(skills),
        "where": location,
        "results_per_page": 20,
        "content-type": "application/json",
    }

    if part_time:
        params["part_time"] = 1
    if full_time:
        params["full_time"] = 1

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()

        jobs = []
        for job in data.get("results", []):
            job_info = {
                "title": job.get("title"),
                "description": job.get("description"),
                "location": job.get("location", {}).get("display_name"),
                "contract_time": job.get("contract_time"),
                "redirect_url": job.get("redirect_url"),
            }
            jobs.append(job_info)

        return jobs

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

if "__main__" == __name__:

    
    jobs = fetch_jobs(
        location='pune',
        skills=['AI','python'],
        part_time=True,
    )

    for job in jobs:
        print(f"Title: {job['title']}")
        print(f"Location: {job['location']}")
        print(f"Contract: {job['contract_time']}")
        print(f"Description: {job['description']}")
        print(f"Apply here: {job['redirect_url']}\n")
