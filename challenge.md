# Capital One Data Challenge

## Instructions to Candidate

The **Data Challenge** will give you an opportunity to showcase your skills and abilities in areas that align with how we challenge our **Data Analysts** at Capital One. We have created the **Data Challenge** to help us find great people to join our team as we continue to develop data products.

As you work on your submission, keep in mind that we will be evaluating every applicant on the following key areas:

### **Evaluation Criteria**
1. **Builder Mindset:** Utilize the right open-source tools to create adaptive and innovative solutions that successfully run. Write code with effective formatting and structure that contains sufficient comments and is concise. Also, write code that leverages functions or other approaches that make it reusable, as well as effectively join datasets.
2. **Data Management:** Systematically perform data quality checks, document issues, and take deliberate steps to resolve issues. In addition, create metadata for any fields that you create.
3. **Business Intelligence:** Create a variety of visualizations that tell a story and provide recommendations that address the business problem. Also, document assumptions and provide ideas for future next steps.

This challenge is your next step in showing Capital One what you can do. You have **1 week** to submit a working data product, per the submission instructions.


## **Problem Statement**
You are working for an airline company looking to enter the **United States domestic market**. Specifically, the company has decided to start with **5 round-trip routes** between **medium and large US airports**. An example of a round-trip route is the combination of **JFK to ORD and ORD to JFK**.

The airline company has to acquire **5 new airplanes** (one per round-trip route), and the upfront cost for each airplane is **$90 million**. The company’s motto is **“On time, for you”**, so punctuality is a big part of its brand image.

You have been tasked with analyzing **1Q2019 data** to identify:

1. **The 10 busiest round-trip routes** in terms of the number of round-trip flights in the quarter. Exclude canceled flights when performing the calculation.
2. **The 10 most profitable round-trip routes** (without considering the upfront airplane cost) in the quarter. Along with the profit, show total revenue, total cost, summary values of other key components, and total round-trip flights in the quarter for the top 10 most profitable routes. Exclude canceled flights from these calculations.
3. **The 5 round-trip routes that you recommend** to invest in based on any factors that you choose.
4. **The number of round-trip flights it will take to break even** on the upfront airplane cost for each of the 5 round-trip routes that you recommend. Print key summary components for these routes.
5. **Key Performance Indicators (KPIs)** that you recommend tracking in the future to measure the success of the round-trip routes that you recommend.


## **Datasets & Metadata**
**[GitHub Link to Datasets](https://github.com/CapitalOneRecruiting/DA-Airline-Data-Challenge)**

### **Datasets Provided:**
1. **Flights Dataset:** Contains data about available routes from origin to destination. Use this dataset for **occupancy calculations**.
2. **Tickets Dataset:** Contains **ticket price data** (sample data only, as the data is huge). Consider only **round trips** in your analysis.
3. **Airport Codes Dataset:** Identifies whether an airport is considered **medium or large** sized. Consider only **medium and large airports** in your analysis.

When **joining these datasets together**, use your **best judgment** on the join condition and document your choice.


## **Assumptions & Constraints**
- Each **airplane is dedicated** to **one round-trip route** between two airports.
- **Costs:**
  - **Fuel, Oil, Maintenance, Crew:** $8 per mile total.
  - **Depreciation, Insurance, Other:** $1.18 per mile total.
  - **Airport operational costs:**
    - **Medium airports:** $5,000 per landing.
    - **Large airports:** $10,000 per landing.
    - A **round-trip flight** has **two airport charges** (one per landing).
  - **Delay costs:**
    - **First 15 minutes** of delay is **free**.
    - Each **additional minute** costs **$75**.
- **Revenue:**
  - Each plane can accommodate **up to 200 passengers**.
  - Each flight has an associated **occupancy rate** (from the Flights dataset).
  - **Baggage fee:**
    - $35 per checked bag per flight.
    - **50% of passengers** check **1 bag per flight**.
    - A round-trip flight incurs **$70 per passenger** for baggage fees.
  - **Disregard seasonal effects** on ticket prices.


## **Solution Approach**

### **1. Data Quality Checks**
- Identify and address at least **3 material data issues** that could impact recommendations.
- Create **metadata** for any new fields added during analysis.

### **2. Data Munging & Joining**
- Write a function to **link datasets in a scalable way**.

### **3. Visual Data Narrative**
- Generate **charts and plots** in Python/R/Tableau.
- Summarize **key trends and insights** using visualizations.
- Show **key metric drivers** behind the final recommended round-trip routes.

### **4. Final Recommendations**
- Identify **both origin and destination airports** for the **5 recommended routes**.
- Provide detailed responses for the **4 additional questions** in the problem statement.

### **5. Future Steps & Next Actions**
- Identify what additional work could be done if **more time was available**.


## **Data & Tools**
- Do **not use any external data** beyond the provided datasets.
- Use **only free and legal tools** (e.g., Python, R, Tableau Public).
- Ensure all work **abides by applicable laws and regulations**.


## **Submission Instructions**
To submit your work, email a **single ZIP file (<10 MB)** to:

📩 **dataanalysisrecruitingmailbox@capitalone.com**

Your ZIP file should contain:
1. **Working source code files**, accompanying documentation, and code outputs.
2. **Documentation including metadata** for new data created and data quality insights.
3. **Visualizations** and key insights.


## **Integrity & Confidentiality Disclosure**
- Do **not post your code or documents** to any public repositories.
- Complete the assessment **independently** and **keep all content confidential**.
- Consulting external resources is allowed, but **all work must be your own**.
- Failure to **maintain confidentiality** may result in disqualification.

If you have any questions or need technical support, contact:
📞 **1-800-304-9102**  
📧 **RecruitingAccomodation@capitalone.com**