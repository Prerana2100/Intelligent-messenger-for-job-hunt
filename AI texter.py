# creating an Artificial intelligent system to text with the application user to filter his preferances
print("Hi\nI'm Aisha, your Personal Assistant. \nI'll be helping you through out your journey in this application")
a=input("Please select your requirements\nAre you a fresher or a professional?")
if a=='fresher':
    b=input("are you looking for a full time job or a part time job?")
    if b=='full time':
        c=input('which type of job are you looking for IT or Non IT?')
        if c=='IT':
            d=input('Are you from circuit department?')
            if d=='yes':
              e=input('are you looking for a job at MNC or a Startup?')
              if e=='MNC':
                print('Please send us your resume\nwe will notify you of the job positions based on your skills')
              else:
                print('Please send us your resume\nwe will notify you of the job positions based on your skills')
            else:
              f=input('are you interested in IT jobs?')
              if f=='yes':
                  print('Please send us your resume\nwe will notify you of the job positions based on your skills')
              else:
                  print('Apologies, we provide job opportunities only for IT field')
elif a=='professional':
    h=input('Do you have gap in your profession?')
    if h=='yes':
        i=input('did you work previously?')
        if i=='yes':
            g=float(input('What was your CTC in your Previous company?'))
        else:
            print('Apologies, companies prefer experienced or a fresher')
    else:
        j=float(input('What is your salary expectations per annum?'))
        print('Please send us your resume\nwe will notify you of the job positions based on your skills and experience')
else:
    print('Apologies, companies expect candidates to be a fresher or a professional with no gap')
