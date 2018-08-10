"""
Most, if not all of the user-customizable information for the
wedsite can go in here. This makes it easier to port the
project between weddings. This was created in a rough first
pass, please keep updating as time goes on such that when
we go from one friend's site to another we don't need to do
much other than change this configuration file.

For the sake of gender-neutrality we'll call the two people
getting married Gride and Broom.
"""
import datetime
import lorem

#
# Gride and Broom
#
FIRST_INITIAL = "first_initial"
FIRST_NAME = "first_name"
LAST_NAME = "last_name"

# Gride info
GRIDE = {
	FIRST_INITIAL : "I",
	FIRST_NAME : "I",
	LAST_NAME : "Really",
}

# Broom info
BROOM = {
	FIRST_INITIAL : "U",
	FIRST_NAME : "Love",
	LAST_NAME : "You",
}

#
# Additional Wedding People.
#

# What we're calling the gridesmaids on the site
GRIDESMAIDS_TEXT = "Gridesmaids"

# List of all Gridesmaids
GRIDESMAIDS = (
	{
	    "title" : "Person of Honor",
		"name" : "Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
		"static_img" : "images/team_photos/team_member.jpg",
	},

	{
	    "title" : "Gridesmaid",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
		"static_img" : "images/team_photos/team_member.jpg",
	},

	{
	    "title" : "Gridesmaid",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
		"static_img" : "images/team_photos/team_member.jpg",
	},

	{
	    "title" : "Gridesmaid",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
		"static_img" : "images/team_photos/team_member.jpg",
	},
)

# What we're calling the broomsmen on the site
BROOMSMEN_TEXT = "Broomsmen"

# List of all Broomsmen
BROOMSMEN = (
	{
	    "title" : "Best Person",
		"name" : "Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
		"static_img" : "images/team_photos/team_member.jpg"
	},

	{
	    "title" : "Broomsman",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
		"static_img" : "images/team_photos/team_member.jpg"
	},

	{
	    "title" : "Broomsman",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
		"static_img" : "images/team_photos/team_member.jpg"
	},

	{
	    "title" : "Broomsman",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
		"static_img" : "images/team_photos/team_member.jpg"
	},
)

# List of people you want to be points of contact for your wedding.
#	This list should be *3 people long* for now to work with the default
#	formatting in contacts.html, otherwise feel free to change the formatting
#	in contacts.html
POINTS_OF_CONTACT = (
	{
		"name" : "Contact Person 1",
		"description" : "Typically Best Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712"
	},

	{
		"name" : "Contact Person 2",
		"description" : "Typically Person of Honor",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712"
	},

	{
		"name" : "Contact Person 3",
		"description" : "Some other poor soul",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712"
	},
)

# Designated email for website trouble.
#   If you're reading this you should probably just put your email address here.
ADMIN_EMAIL = "webmaster@wedsite.io"

#
#  Rehearsal Dinner info.
#
REHEARSAL_DINNER = {
	"date" : datetime.datetime(2018, 2, 18, 18, 00, 00), # Year, month, day, hour, minute, second
	"location" : {
		"name" : "Some Restaurant",
		"address" : "1234 Tasty Trail",
		"city" : "Flavortown",
		"state" : "CA",
		"zip" : "00000",
		"maps_link" : "https://www.google.com/maps/place/Lloyd+House/@33.9745866,-118.3231545,11z/data=!4m8!1m2!2m1!1slloyd+house!3m4!1s0x80c2c4a868b87301:0x5857f9f8e8bb154b!8m2!3d34.1371511!4d-118.1228224"
	},
	"additional info" : "None",
}

#
# Wedding Ceremony Info
#
WEDDING_CEREMONY = {
	"date" : datetime.datetime(2018, 2, 18, 18, 00, 00), # Year, month, day, hour, minute, second
	"arrive_by" : datetime.datetime(2018, 2, 18, 15, 45, 00),
	"attire" : lorem.sentence(),
	"details" : lorem.paragraph(),
	"location" : {
		"name" : "Some Venue",
		"address" : "274 Olive Walk",
		"city" : "Pasadena",
		"state" : "CA",
		"zip" : "91125",
		"maps_link" : "https://www.google.com/maps/place/Lloyd+House/@33.9745866,-118.3231545,11z/data=!4m8!1m2!2m1!1slloyd+house!3m4!1s0x80c2c4a868b87301:0x5857f9f8e8bb154b!8m2!3d34.1371511!4d-118.1228224",
		"map_address" : "274 Olive Walk Pasadena, CA 91125", #Yes, this is the same as the regular address. Had trouble making the easy map work. Need to look into it
		"parking" : lorem.sentence(),
	},
	"additional info" : "None",
}

#
# Reception Info
#
WEDDING_RECEPTION = {
	"date" : datetime.datetime(2018, 2, 18, 18, 00, 00), # Year, month, day, hour, minute, second
	"time_end" : datetime.datetime(2018, 2, 19, 00, 00, 00),
	"details" : lorem.paragraph(),
	"location" : {
		"name" : "Perhaps the same venue, perhaps not",
		"address" : "1234 Party Place",
		"city" : "Funtime",
		"state" : "CA",
		"zip" : "00000",
		"maps_link" : "https://www.google.com/maps/place/Lloyd+House/@33.9745866,-118.3231545,11z/data=!4m8!1m2!2m1!1slloyd+house!3m4!1s0x80c2c4a868b87301:0x5857f9f8e8bb154b!8m2!3d34.1371511!4d-118.1228224"
	},
	"additional info" : "None",
}

#
# Explore Info. This section should be a bit lengthier since you're
#	giving guests ideas about how to spend their time for parts of the
#	weekend you haven't directly scheduled.
#
EXPLORE_TITLE = "Explore LA!"

EXPLORE_AREA_1 = {
	"name" : "The South Bay",
	"map_address" : "South Bay, Los Angeles County, CA",
	"description" : lorem.paragraph(),
}

EXPLORE_AREA_2 = {
	"name" : "Downtown",
	"map_address" : "111 S Grand Ave, Los Angeles, CA 90012",
	"description" : lorem.paragraph(),
}

EXPLORE_AREA_3 = {
	"name" : "Westside",
	"map_address" : "Westside, Los Angeles, CA",
	"description" : lorem.paragraph(),
}

#
# Gifts Info. This will change a lot based on what you're looking for
#	out of your gifts page. There are three example gift options below,
#	and you can have as many or few of them as you'd like of any type
#	in any order.
#
GIFT_OPTIONS = (

	# Basic Gift option. Text only
	{
		"name" : "Cultural Tradition",
		"description" : lorem.paragraph(),
	},

	# Gift option with a hyperlinked image
	{
		"name" : "Registry",
		"description" : lorem.paragraph(),
		"image" : {
			"hyperlink" : "https://wedsite.io",
			"static_img" : "images/amazon_registry.png"
		},
	},

	# Gift option with a video
	{
		"name" : "Donations",
		"description" : lorem.paragraph(),
		"video" : {
			"hyperlink" : "https://www.youtube.com/embed/Uoq2EG3BpS4"
		},
	},
)

#
# Main Page Info
#
LANDING_PAGE = {
    "background_image": "images/main_jumbotron.jpg",
    # which horizontal third should info be placed in? can be "left" or "right"
    "info_pos": "center",
    "info_margin_top": "100px", # vertical position of top of info box
    "info_color": "#fff",
}

#
# RSVP Page Info
#

# RSVP Cutoff Date
RSVP_CUTOFF_DATE = datetime.datetime(2018, 2, 18)

# Whether or not the RSVP portion of the site is active. If this is False
#	then it will show users their RSVP but will not allow them to edit it,
#	else when true they can edit it. This could eventually be modified
#	to be automatically calculated from the cutoff but timezones get 
#	tricky so for now we need to manually change it over
RSVP_ACTIVE = True

# Meal Description. Use this to go over your menu options or explain
#	about the family-style menu, buffet, etc.
MEAL_DESCRIPTION = "All meals will be served family-style"

# Food Choices. These will be the labels and descriptions used for options on
#       the RSVP. If there are no options (e.g. because it's all family style),
#       use the MEAL_DESCRIPTION to note this and leave this as an empty list.
FOOD_CHOICES = [
    ("Steak", "New York Strip with fancy potatoes and probably something green"),
    ("Salmon", "Alaskan Salmon. What else do you need?"),
    ("Vegetarian", ""), # an option lacking further description in the header
]

#
# Story Page Info. Recommended to keep this to multiples of 3
#	to look best. Try to also keep all paragraphs the same length
#
STORY_ITEMS = (
	{
		"title" : "Story Item 1",
		"description": lorem.paragraph(),
	},
	{
		"title" : "Story Item 2",
		"description": lorem.paragraph(),
	},
	{
		"title" : "Story Item 3",
		"description": lorem.paragraph(),
	},
	{
		"title" : "Story Item 4",
		"description": lorem.paragraph(),
	},
	{
		"title" : "Story Item 5",
		"description": lorem.paragraph(),
	},
)

#
# Credits for the team page
#
CREDITS_TEXT = "Thank you to all of our family and friends who have helped make our wedding special! We would like to thank a few of our friends whose work you all have seen."
CREDITS_ITEMS = (
	{
		"name" : "Awesome Friend 1",
		"item" : "Thing awesome friend 1 did",
	},

	{
		"name" : "Awesome Friend 2",
		"item" : "Thing awesome friend 2 did",
	},
)

#
# Traditions page. Explanation of various cultures' traditions
#
TRADITIONS_ITEMS = (
	{
		"name" : "Culture 1 Traditions",
		"items" : (
			{
				"name" : "item 1",
				"description" : lorem.paragraph(),
			},
			{
				"name" : "item 2",
				"description" : lorem.paragraph(),
			},
			{
				"name" : "item 3",
				"description" : lorem.paragraph(),
			},
		),
	},
	{
		"name" : "Culture 2 Traditions",
		"items" : (
			{
				"name" : "item 1",
				"description" : lorem.paragraph(),
			},
			{
				"name" : "item 2",
				"description" : lorem.paragraph(),
			},
			{
				"name" : "item 3",
				"description" : lorem.paragraph(),
			},
		),
	},
)

#
# Travel Page. All of the info your guests may need for travel and
#	lodging
#
AIRPORT_INFO = lorem.paragraph()

HOTEL_ITEMS = (
	{
		"name" : "Hotel 1",
		"city" : "Romanticville",
                "link_title" : "Yelp Page",
		"link" : "https://www.yelp.com/",
		"phone" : "(626)-395-1712",
		"mention" : "Group Discount Name",
		"discount" : "100%",
		"description" : lorem.paragraph(),
	},

	{
		"name" : "Hotel 2",
		"city" : "Romanticville",
                "link_title" : "Yelp Page",
		"link" : "https://www.yelp.com/",
		"phone" : "(626)-395-1712",
		"mention" : "Group Discount Name",
		"discount" : "100%",
		"description" : lorem.paragraph(),
	},
)

AIRBNB_LINK = "https://airbnb.com/"

#
# Which favicon to use
#
FAVICON = "images/favicons/favicon-heart.ico"

#
# Top-level Object that's fed into the templates
#

DEFAULT_JSON = {
	"gride" : GRIDE,
	"broom" : BROOM,
	"gridesmaids" : {
		"text" : GRIDESMAIDS_TEXT,
		"team" : GRIDESMAIDS,
	},
	"broomsmen" : {
		"text" : BROOMSMEN_TEXT,
		"team" : BROOMSMEN,
	},
	"contact" : POINTS_OF_CONTACT,
	"rehearsal" : REHEARSAL_DINNER,
	"ceremony" : WEDDING_CEREMONY,
	"reception" : WEDDING_RECEPTION,
	"explore" : {
		"title" : EXPLORE_TITLE,
		"areas" : (
			EXPLORE_AREA_1,
			EXPLORE_AREA_2,
			EXPLORE_AREA_3,
		),
	},
	"gifts" : GIFT_OPTIONS,
	"landing_page" : LANDING_PAGE,
	"rsvp" : {
		"cutoff" : RSVP_CUTOFF_DATE,
		"active" : RSVP_ACTIVE,
		"meal_description_header" : MEAL_DESCRIPTION,
                "comments_prompt": "Please use the section below to add a general comment to your response.",
                # NB these fields must correspond to acutal columns. you can
                # relabel/filter them, but don't add new ones without changing
                # the RSVPPerson model as well
                "fields": {
                    "name": "Name",
                    "is_attending_rehearsal": "Attend Rehearsal Dinner?",
                    "is_attending_wedding": "Attend Wedding?",
                    "is_child": "Child?",
                    "dietary_vegetarian": "Vegetarian",
                    "dietary_vegan": "Vegan",
                    "dietary_kosher": "Kosher",
                    "dietary_gluten_free": "Gluten Free",
                    "dietary_other": "Other Dietary Restriction",
                    "special_requests": "Special Request",
                },
                "food_options": FOOD_CHOICES,
	},
	"story" : STORY_ITEMS,
	"credits" : {
            "text": CREDITS_TEXT,
            "people": CREDITS_ITEMS,
        },
	"traditions" : TRADITIONS_ITEMS,
	"travel" : {
		"airport_info" : AIRPORT_INFO,
		"hotels" : HOTEL_ITEMS,
		"airbnb_link" : AIRBNB_LINK,
	},
	"favicon" : FAVICON,
        "admin_email": ADMIN_EMAIL,
        # Which pages have restricted access
        #   Valid values are 'all', 'login', and False for no access at all
        #   False may be desired if you don't want to use a page at all for the duration
        #   of your wedding, or if it simply doesn't exist yet (e.g. for save the dates)
        "access": {
            "index" : "all",
            "contact" : "login",
            "story" : "login",
            "wedding" : False,
            "events" : False,
            "travel" : "login",
            "explore" : False,
            "gifts" : False,
            "team" : False,
            "traditions" : False,
        },
}

# if an app does not override WEDSITE_JSON, use DEFAULT_JSON
WEDSITE_JSON = DEFAULT_JSON
