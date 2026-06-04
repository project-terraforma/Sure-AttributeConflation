# Sure-AttributeConflation
## Overview of the Project
* Problem Statement: Places attribute conflation (PAC) issue handles duplicate records of the same real-world entity from different sources. Attributes can range from addresses to websites, and issues can range from format errors to staleness checks and beyond.

An example includes:
- "99 Ranch Market" vs "99 Ranch market" 
- Different phone numbers
- Missing websites or leading to another page that's not active

## OKRs
### Objective 1: Analyze and understand dataset characteristics
_Key Results:_
* Analyze 2,000 labeled records from the Mayhem dataset and corresponding Overture place records
* Examine at least 5 key attributes (names, phones, websites, addresses, and categories) for missing values, formatting differences, and inconsistencies
* Quantify the distribution of "same", "current", and "base" labels and identify at least 3 recurring patterns that influence attribute selection decisions
* Investigate relationships between current and base attributes across 1,000+ place pairs to understand attribute quality and selection behaviors
### Objective 2: Develop and evaluate attribute selection models
_Key Results:_
* Implement and compare at least 3 approaches: rule-based, similarity-based, and machine learning models
* Establish a baseline accuracy of at least 60% using rule-based methods and at least 65% using similarity-based classification
* Train a machine learning model on approximately 2,000 labeled records and achieve at least 70% accuracy
* Improve overall attribute selection performance to at least 80% accuracy through feature engineering, enhanced rules, or model combination techniques

