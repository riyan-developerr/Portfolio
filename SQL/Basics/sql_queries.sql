/*
This is the record some of my last queries completing the basics setion of sql course by Luke Barousse

*/
-- =====================================================================================
-- for null values
SELECT 
	job_id as ID, 
    job_title as Title, 
    salary_year_avg as Average_Yearly_Salary, 
    salary_hour_avg 
FROM
	job_postings_fact 
WHERE
	(Average_Yearly_Salary is not NULL) and (salary_hour_avg is not NULL);

-- =====================================================================================
-- Left join 

select 
	job_postings_fact.job_id, 
    job_postings_fact.company_id ,
    company_dim.name
From
	job_postings_fact
left join company_dim
	on job_postings_fact.company_id = company_dim.company_id;

-- =====================================================================================
SELECT 
	job_postings.job_title_short, 
    company.name
FROM
	job_postings_fact as job_postings 
LEFT JOIN company_dim as company 
	on job_postings.company_id = company.company_id 
WHERE
	job_postings.job_title_short = 'Data Analyst'

-- =====================================================================================
select 
	job_postings_fact.job_title_short,
	skills_dim.skills
from job_postings_fact 
LEFT JOIN skills_job_dim on job_postings_fact.job_id = skills_job_dim.job_id 
LEFT JOIN skills_dim on skills_job_dim.skill_id = skills_dim.skill_id

WHERE
	job_postings_fact.job_title_short = 'Data Analyst'

-- =====================================================================================

-- NOw the final Query of Basics Chapter

/* 
First get the names of skills 
then find the total jobs for those skills
also groupby so when we do sum it will find the sum of job postings for a particular skill
then find the averge salary for each skill 
finally order by salary
*/
SELECT 
	skills.skills, 
    COUNT(skills_job.job_id) as Job_Postings, 
    AVG(job_postings_fact.salary_year_avg) as Average_Salary
FROM skills_dim as skills 
LEFT JOIN skills_job_dim as skills_job on skills.skill_id = skills_job.skill_id
LEFT JOIN job_postings_fact on job_postings_fact.job_id = skills_job.job_id

GROUP BY skills.skills
ORDER BY Average_Salary DESC

-- =====================================================================================