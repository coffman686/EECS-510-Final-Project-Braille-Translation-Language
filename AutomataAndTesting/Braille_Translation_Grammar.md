# Grammar for the Language

## The following is the formal grammar written for our language:

**S**     ->  0**Q32** | 1**Q1** | λ  

**Q1**   ->  0**Q2** | 1**Q11**  

**Q2**   ->  0**Q3** | 1**Q7**  

**Q3**   ->  0**Q4** | 1**Q19**  

**Q4**   ->  0**Q5** | 1**Q41**  

**Q5**   ->  0**S**  

**Q7**   ->  0**Q8** | 1**Q29**  

**Q8**   ->  0**Q9** | 1**Q43**  

**Q9**   ->  0**S**  

**Q11**  ->  0**Q12** | 1**Q22**  

**Q12**  ->  0**Q13** | 1**Q16**  

**Q13**  ->  0**Q14** | 1**Q45**  

**Q14**  ->  0**S**  

**Q16**  ->  0**Q17** | 1**Q47**  

**Q17**  ->  0**S**  

**Q19**  ->  0**Q20** | 1**Q49**  

**Q20**  ->  0**S**  

**Q22**  ->  0**Q23** | 1**Q26**  

**Q23**  ->  0**Q24** | 1**Q51**  

**Q24**  ->  0**S**  

**Q26**  ->  0**Q27** | 1**Q53**  

**Q27**  ->  0**S**  

**Q29**  ->  0**Q30** | 1**Q55**  

**Q30**  ->  0**S**  

**Q32**  ->  1**Q33**  

**Q33**  ->  1**Q34**  

**Q34**  ->  0**Q35** | 1**Q38**  

**Q35**  ->  0**Q36** | 1**Q57**  

**Q36**  ->  0**S**  

**Q38**  ->  0**Q39** | 1**Q59**  

**Q39**  ->  0**S** | 1**S**  

**Q41**  ->  0**S** | 1**S**  

**Q43**  ->  0**S** | 1**S**  

**Q45**  ->  0**S** | 1**S**  

**Q47**  ->  0**S** | 1**S**  

**Q49**  ->  0**S** | 1**S**  

**Q51**  ->  0**S**  

**Q53**  ->  0**S**  

**Q55**  ->  0**S**  

**Q57**  ->  0**S**  

**Q59**  ->  0**S**  
