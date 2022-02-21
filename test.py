import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
data = {
    "Inputs": {
        "data":
        [
            {
                'text': "after 9 months of hard core islam muslim clock boy returns to tx still plans to sue state he misses for 15 millioncair s poster child for how to use islam to get everything you want in politically correct america comes home obama boot camp ahmed mohamed the teen known as clock boy may be back in texas within days after nine months of living in his new homeland qatar he reportedly feels homesick late friday the dallas morning news reported mohamed plans to return to texas early in the week for an extended visit the teen s uncle aldean mohamed said he miss texas and he miss irving breitbart texas reported on ahmed mohamed s earlier yearnings to return to the lone star state in december the uncle also indicated his nephew will catch up with family in the dallas suburb of irving and has events lined up with some tech companies the dallas newspaper did not disclose any information with whom the teen will meet ahmed mohamed was the 14 year old irving independent school district high school freshman detained last september for bringing to class a makeshift clock in a box which school officials and police initially believed was a hoax bomb no charges were filed once the situation sorted itself out but the teen served three days of suspension before his family decided to withdraw him from the school district a subsequent media firestorm ensued in which mainstream news outlets insisted islamophobia was behind mohamed s detainment breitbart texas maintained it was the result of rigid public school zero tolerance policies and a month later the associated press agreed last october mohamed accepted a fully funded education scholarship from the qatar foundation an organization with reputed ties to the muslim brotherhood over an invitation to the one of the world s most prestigious private research universities the massachusetts institute of technology mit this year mit ranked 1 across twelve fields of study with other disciplines placing in the top five internationally fueled by the progressive narrative of victimization mohamed traveled to google s northern california headquarters toured the qatari educational system he now attends made a saudi funded pilgrimage to mecca rubbed shoulders with sudanese islamic autocrat bashir appeared in a council on american islamic relations cair promo video with executive director nihad awad a supporter of the palestinian terrorist group hamas and attended cair s 2015 champions for justice gala in arlington va then mohamed visited the white house for astronomy night where he met president obama alongside other invited students previously the commander in chief tweeted the teen should bring his cool clock with him but that was not possible the family did not retrieve it until late october despite the irving police department s requests for them to do so a month earlier while in washington d c uncle aldean ahmed and his father mohamed elhassen mohamed rallied with uber left california u s rep mike honda who pushed for a doj probe into the irving school district and police department regarding the legality of the teen s detainment time magazine listed mohamed on their 30 most influential teens of 2015 yet by december with the christmas season shrouded by islamic state attacks in paris state department travel alerts and syrian refugees at u s borders sympathy waned for the islamophobia poster child breitbart news reported that the same liberal media that championed mohamed s every move lost interest according to the dallas morning news uncle aldean mohamed said the family still plans to sue the irving isd over ahmed s arrest after they left for qatar the mohamed family demanded a total of 15 million 10 million from the city of irving and 5 million from the school district and threatened a lawsuit if they did not receive it in a 10 page letter to the irving city attorney and a similar 9 page letter to irving isd s attorney the family claimed islamophobia among their clock related incident allegations via bretibart news",
            },
        ],
    },
    "GlobalParameters": {
        'method': "predict",
    }
}

body = str.encode(json.dumps(data))

url = 'http://0c49f0df-7902-43e5-9143-b677c007aadb.southeastasia.azurecontainer.io/score'
api_key = '' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
