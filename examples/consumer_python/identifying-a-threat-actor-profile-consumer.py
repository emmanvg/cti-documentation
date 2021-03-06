from stix2.v21 import (Bundle)

for obj in bundle.objects:
    if obj == threat_actor:
        print("------------------")
        print("== THREAT ACTOR ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Name: " + obj.name)
        print("Description: " + obj.description)
        print("Threat Actor Types: " + str(obj.threat_actor_types))
        print("Aliases: " + str(obj.aliases))
        print("Roles: " + str(obj.roles))
        print("Goals: " + str(obj.goals))
        print("Sophistication: " + obj.sophistication)
        print("Resource Level: " + obj.resource_level)
        print("Primary Motivation: " + obj.primary_motivation)

    elif obj == identity:
        print("------------------")
        print("== IDENTITY ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Name: " + obj.name)
        print("Description: " + obj.description)
        print("Identity Class: " + obj.identity_class)
        print("Contact Information: " + obj.contact_information)

    elif obj == relationship:
        print("------------------")
        print("== RELATIONSHIP ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Type: " + obj.type)
        print("Relationship Type: " + obj.relationship_type)
        print("Source Ref: " + obj.source_ref)
        print("Target Ref: " + obj.target_ref)
