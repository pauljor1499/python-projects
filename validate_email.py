'''
• 1. valid email address
• 2. malformed email address      yraheem*yahoo.com
• 3. short email address    y@yahoo.com
  4. invalid domain   yraheem@thisismyowndomainthatIcreatedonTuesday.com
  5. another valid domain yraheem@yahoo.net
  6. numeric email   13143241234@142341234.com
  7. valid email  yraheem.ammon@yahoo.com
  8. invalid email  yraheem.ammon@yahoo.com.net
• 9. invalid email  yraheem@yahoo
  10. valid alpha numeric   dsfsadfsadfsafs@dfasdad.com
  11. valid alpha numeric   tommy3838@yahoo.com
• 12. blank email  ""
  13. special characters  lasjd!!!!111@gmail.com?
• 14. begin with special characters  *((&&(&(&))))@yahoo.com
• 15. two dots   y...raheem@yahoo.com   (invalid)
• 16. underscore    y_raheem@yahoo.com
• 17. more than 3 char (domain)   yraheem@yahoo.comm
pauljor@g.cjc.edu.ph
'''

class Verify:

  @staticmethod
  def validate_email(email: str):
    verified = False
    divide_email: list = email.split("@")
    divide_email_domain: list = divide_email[1].split(".")
    special_characters: str = "!#$%&'*+-/?^_{|."
    allowed_letter_domain = ['g', 'y', 'r']
    allowed_workspace_domain = ['cjc', 'ppl', 'prs']
    allowed_domain = ['com', 'net', 'org', 'edu']
    allowed_country_domain = ['ph', 'us', 'fr', 'esp']
    try:
        # Check email is not empty or contains '@' and '.'
        if(email != '' or "@" in email or "." in email):

            # Check email has only one '@'
            if(email.count('@') == 1):

                # Check email user name is >= 1 and <= 15 AND Check email domain is >= 3 and <= 15
                if((len(divide_email[0]) >= 3 and len(divide_email[0]) <= 15) and (len(divide_email[1]) >= 3 and len(divide_email[0]) <= 15)):
                    
                    # Check email user name
                    if(divide_email[0]): 

                        for char in divide_email[0]:
                            if(char in special_characters):
                                return "Invalid email characters"

                        # Check email domain contains 1 '.'
                        if(divide_email[1].count('.') == 1 ):

                            if(divide_email_domain[1] in allowed_domain):
                                print(divide_email_domain)
                                return "Email is valid"

                            else:
                                return "Invalid domain"

                        # Check email domain contains 3 '.'
                        elif(divide_email[1].count('.') == 3):

                            if(divide_email_domain[0] in allowed_letter_domain):

                                if(divide_email_domain[1] in allowed_workspace_domain):

                                    if(divide_email_domain[2] in allowed_domain):

                                        if(divide_email_domain[3] in allowed_country_domain):

                                            print(str(divide_email) +" "+ str(divide_email_domain))
                                            return "Email is valid"
                                
                                        else:
                                            return "Invalid country domain"
                                    else:
                                        return "Invalid domain"
                                else:
                                    return "Invalid workspace domain"
                            else:
                                return "Invalid letter domain"
                        else:
                            return "Invalid email domain"
                    else:
                        return "Invalid email characters"
                else:
                    return "Invalid email length"
            else:
                return "Multiple @ or Invalid '.'"
        else:
            return "Empty email or no '@' or no '.'"
    except Exception as error:
            print(f"Error from -> validate_email(): {error}")
    

email: str = input("Enter email: ")
print(Verify.validate_email(email))
