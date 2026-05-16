# Sure-AttributeConflation
## Overview of the Project
* Project A: In this project, I will focus on resolving issues with conflicting information about the same place across different sources (Google Maps, Yelp, Apple Maps, etc.).
* Definition: When different sources provide slightly different information (i.e. phone numbers, names, websites), it gets confusing on what information is accurate. The goal of this project is to fix exactly that by creating something that can select the most accurate and reliable version.

## Problem
A single place can have multiple records from different sources with different information.

An example includes:
- "99 Ranch Market" vs "99 Ranch market" 
- Different phone numbers
- Missing websites or leading to another page that's not active

## OKRs
# <ins>Objective 1: Explore, understand, and compare datasets</ins>
_Key Results:_
    * Load and explore the datasets (Mayhem and Overture) to identify key attributes (name, phone number, website)
    * Compare data quality (i.e. missing values and formatting differences)
    * Analyze label distribution (i.e. “same” vs. “current”) and record structure (base_id grouping)
# <ins>Objective 2: Develop and compare attribute selection methods</ins>
_Key Results:_
    * Implement a simple-rule based baseline for attribute selection
    * Add a similarity-based approach (i.e. name similarity using RapidBuzz)
    * Evaluate both methods using accuracy and compare their performance
# <ins>Objective 3: Analyze performance and identify improvements</ins>
_Key Results:_
    * Identify 1-2 common failure cases
    * Can be formatting differences vs. real conflicts
    * Explain when each method performs better or worse
    * Propose 1-2 improvements based on observed results

