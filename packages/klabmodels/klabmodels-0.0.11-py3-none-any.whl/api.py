from datetime import datetime
from klabmodels import Candidate, JobDescription, Interview, Questionnaire, CVEvaluation, Company
from langroid.agent.chat_document import ChatDocument
from typing import Dict, List
import logging
import time


## Store data to Redis
##

def persist_job_description(reference: str, title: str, company_name: str, **kwargs):
   """
   Persist a job description
   """
   try:
      jd = JobDescription.find(JobDescription.reference==reference).first()
      logging.info(f"Found job: {reference}")
      jd.job_title = title
      jd.company = company_name
      if kwargs: jd.__dict__.update(kwargs)
   except:
      logging.info(f"Not Found job: {reference}")
      if 'job_title' in kwargs: kwargs.pop('job_title', None)
      jd = JobDescription(reference=reference, job_title=title, company=company_name, **kwargs)
   finally:
      jd.save()
   return jd

def persist_candidate(name: str, **kwargs):
   """
   Persist a candidate
   """
   try:
      c = Candidate.find(Candidate.name==name).first()
      if 'name' in kwargs: del kwargs['name']
      c.__dict__.update(kwargs)
   except:
      c = Candidate(name=name, **kwargs)
   finally:
      c.save()
   return c
   



def persist_questionnaire(job: JobDescription, candidate: Candidate, questions: Questionnaire):
    """
    Save Interview questionnaire creation to Redis DB
    Args:
      job: (str) Job Description
      candidate: (Candidate) name and resume
      questions (Questionnaire): generated interview questions

    Returns: 
      interview_pk: (pk) interview id to be used to generate a link for the candidate interview
    """
    #user = cl.user_session.get("account")

    interview = Interview( 
                  date=time.time(), 
                  candidate=candidate.pk, 
                  job_description=job.pk,
                  questions=questions,
                  #uuid=interview_id
                  )
       
    interview.save()
    return interview


def persist_interview(interview_pk: str, dialogue: List[ChatDocument]):
    """
    
    """
    #user = cl.user_session.get("account")
    try:
      interview = Interview.find(Interview.pk==interview_pk).first()
      interview.interview =[msg for msg in dialogue if msg.role in ('user', 'assistant')]
      interview.save()
      logging.info(f"Interview saved for {interview.candidate} with {len(dialogue)} documents.")
    except Exception as e:
       logging.error(f"Error persisting interview: {str(e)}")


def persist_interview_evaluation(interview_pk: str, evaluation: List[Dict]):
    """
    Store an interview evaluation on Redis
    """
    #user = cl.user_session.get("account")
    try:
      interview = Interview.find(Interview.pk==interview_pk).first()
      interview.evaluation = evaluation
      interview.save()
      logging.info(f"Interview evaluation saved for {interview.candidate}.")
    except Exception as e:
       logging.error(f"Error persisting interview: {str(e)}")
    

def persist_cv_evaluation(candidate_pk: str, job_description_pk:str, evaluation:Dict):
   """
   Store a CV evaluation grading and summary on Redis
   """
   cv_evaluation = None
   try:
      cv_evaluation = CVEvaluation.find(CVEvaluation.candidate==candidate_pk and CVEvaluation.jobdesc==job_description_pk).first()
      cv_evaluation.grade = evaluation.get('grade')
      cv_evaluation.comments = evaluation.get('comments')
   except Exception as e:
      logging.info(f"Adding CV evaluation for candidate {candidate_pk}...")
      cv_evaluation = CVEvaluation(candidate=candidate_pk,
                                   jobdesc=job_description_pk,
                                   grade=evaluation.get('grade'),
                                   summary=evaluation.get('summary'))
   finally:
    if cv_evaluation:
       cv_evaluation.save()
   


def persist_company(name: str, **kwargs):
   """
   Save Company info
   """
   try:
      company = Company.find(Company.name==name).first()
      logging.info(f"Found existing company {name}")
      company.__dict__.update(kwargs)
   except Exception as e:
      logging.info(f"Saving new company {name}: {str(e)}")
      company = Company(name=name, **kwargs)
   finally:
      company.save()
   return company


## Retrieve data

def get_interview_from_id(interview_id: str):
  """
  Retrieves stored interview
  """
  logging.info(f"Looking for interview {interview_id}")
  try:
    interview = Interview.find(Interview.pk==interview_id).first()
    return interview
  except Exception as e:
    logging.error(f"Interview {interview_id} not found")
    print(e)

def get_user_interviews(with_answers=True):
    """
    Retrieve generated questionnaires for a user
    """
    #user = cl.user_session.get("account")
    try:
      #interviews = Interview.find(Interview.user==user).all()
      interviews = Interview.find().all()
      logging.info(f"Retrieved {len(interviews)} interviews.")
      if interviews:
         if with_answers:
          i_list = [i for i in interviews if i.interview]
         else:
          i_list = [i for i in interviews if not i.interview]
         return i_list

    except Exception as e:
        logging.error(f"No interviews retrieved: {str(e)}")
        return None


def get_candidates_interviews_to_eval():
    """
    Retrieve generated questionnaires for a user
    """
    #user = cl.user_session.get("account")
    try:
      #interviews = Interview.find(Interview.user==user).all()
      interviews = Interview.find().all()
      interviews = [i for i in interviews if i.interview!=[]]
      logging.info(f"Retrieved {len(interviews)} interviews to evaluate")
      if interviews:
         candidates = [Candidate.find(Candidate.pk==i.candidate).first() for i in interviews]
         jobs = [JobDescription.find(JobDescription.pk==i.job_description).first() for i in interviews]
         return interviews, candidates, jobs
      else:
        logging.info(f"No interviews retrieved: {str(e)}")
        #return None

    except Exception as e:
        logging.error(f"No interviews retrieved: {str(e)}")
        #return None


def get_jobs_descriptions(company: str):
   """
   Get Job Descriptions that have been processed to json format
   """
   #user = cl.user_session.get("account")
   try:
      jobs = JobDescription.find(JobDescription.company==company).all()
      if jobs:
        # some filter
        #jobs = [j for j in jobs if j.reference=='']
        return jobs
      else:
         logging.error(f"No jobs retrieved.")
   except Exception as e:
    logging.error(f"No jobs retrieved.")
    return None


def get_candidates(job_reference: str):
   """
   Get candidates who have applied for a job whose CV have been processed to json format
   """
   #user = cl.user_session.get("account")
   try:
      candidates = Candidate.find().all()
      if candidates:
        candidates = [c for c in candidates if c.resume_classified] # CV has been processed
        candidates = [c for c in candidates if job_reference in c.jobs_applied] # Has applied for the job
        if candidates:
          return candidates
        else:
           logging.error(f"No candidates retrieved for the job position {job_reference}.")    
      else:
         logging.error(f"No candidates retrieved.")
   except Exception as e:
    logging.error(f"No candidates retrieved.")
    return None


def apply_for_a_job(candidate_pk:str, job_reference: str):
  """
  A candidate applies for a job
  """
  try:
    candidate = Candidate.find(Candidate.pk==candidate_pk).first()
    if job_reference not in candidate.jobs_applied:
       candidate.jobs_applied.append(job_reference)
       candidate.save()
       logging.info(f"Candidate {candidate_pk} job application for job {job_reference} submitted.")
  except Exception:
     logging.error(f"Candidate {candidate_pk} not found.")
     

def getCompany(name: str):
   """
   Retrieve a company by name
   """
   try:
      company = Company.find(Company.name==name).first()
      return company
   except Exception as e:
      logging.info(f"Company {name} not found.")
