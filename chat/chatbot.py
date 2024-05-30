def handle_user_input(input_text):
    intent = input_text
    if intent == "1":
        # Handle admission intent
        response = 'For admission enquiry <a href="https://gmiu.edu.in/gmiu/admission/" target="_blank">click here</a>'
    elif intent == "2":
        # Handle placement intent
        response = 'For placement statatics <a href="https://gmiu.edu.in/placement/placement-overview-and-statistics" target="_blank">click here</a>'
    elif intent == "3":
        # Handle branch info intent
        response = 'For branch info <a href="https://gmiu.edu.in/admission/courses-offered" target="_blank">click here</a>'
    elif intent == "4":
        # Handle faculty info intent
        response = 'To get faculty information contact us on :<br />Call on :+91 90999 51160 ; +91 75749 49494<br />Mail on : info@gmiu.edu.in<br />Address : Survey No. 30, Sidsar Road, Bhavnagar Gujarat(India)'
    elif intent == "5":
        # Handle contact info intent
        response = 'To contact us :<br />Call on :+91 90999 51160 ; +91 75749 49494<br />Mail on : info@gmiu.edu.in<br />Address : Survey No. 30, Sidsar Road, Bhavnagar Gujarat(India)'
    else:
        response = "<div>[1] . Admission Inquiry</div><div>[2] . Placement Statatics</div><div>[3] . Courses We Offer</div><div>[4] . Our Faculties</div><div>[5] . Contact Us</div>Press any key between [1] to [5]"

    return response
