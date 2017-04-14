# Hello everyone! Welcome to this session of Strings in Python Programming with a Panda!
# This time we're going to have a quick look at the 'Strings' data type
# in Python, and how we can manipulate them.

# Let's start with defining Strings in Python. Till now, we've looked at different numerical types.
# Strings are basically just a sequence of textual data (characters, which may include numbers).

# Strings can be initialized and defined in a number of ways in Python:

firstName = 'Kevin';        # A String sequence can be initialized using single quotes (' ').
lastName = "Sequeira";      # A String sequence can be initialized using double quotes (" ").
print('First Name: ' + firstName);
print('Last Name: ' + lastName);

fullName = firstName + ' ' + lastName;      # String sequences can be concatenated to form larger Strings.
                                            # A close look will tell you that it doesn't matter if the individual
# String sequences were differently created and defined.
print('Full Name: ' + fullName + '\n');

description = '''Hey everyone! I'm an Acquisition Editor at Packt Publishing.
I've formerly been a Developer at a leading MNC,
and I'm interested in Python, Java, R, and various front-end technologies!''';
print('Description: ' + description + '\n');

# String sequences can also be initialized using triple single quotes ('''  ''')
# and these can span multiple lines of code. This means the output of the above code is:
# Description: Hey everyone! I'm an Acquisition Editor at Packt Publishing.
# I've formerly been a Developer at a leading MNC,
# and I'm interested in Python, Java, R, and various front-end technologies!

# Well, the same applies to initializing Strings in triple double quotes ("""  """).
metaDescription = """Engineer / Acquisition Editor / Web Developer / 
Son / Lover / Brother / Friend / Christian / Indian /
Fat"""
print('Meta Description: ' + metaDescription + '\n');

# A deeper definition of Strings would be such: A sequence of characters that are positionally
# ordered and has a finite length once defined.

# Yes, Strings are a sequence of characters with postion numbers assigned to these characters.
# These position numbers, known as indexes are ordered from left-to-right, like a number line
# starting from zero (0).
# Let's take the String 'fullName' we'd defined earlier:

print('First Character of Full Name: ' + fullName[0]);
print('Second Character of Full Name: ' + fullName[1]);
print('Third Character of Full Name: ' + fullName[2]);
print('Fourth Character of Full Name: ' + fullName[3]);
print('Fifth Character of Full Name: ' + fullName[4]);
print('Sixth Character of Full Name: ' + fullName[5]);
print('Seventh Character of Full Name: ' + fullName[6] + '\n');

# I believe the above five lines of code make it easy to understand how String positions
# are numbered.

# You can even fetch the length - the number of characters within a String - using the
# 'len()'function.
nameLength = len(fullName);
print('Length of Full Name: ' + str(nameLength) + '\n');   # Remember, the length that is fetched using the 'len()'
                                                    # function is a number. So we've converted it to a String in this
# print() statement.

# So now that we've understood what Strings are, and why they are called Sequences,
# let's look at a the different (but not all) operations that can be performed on Strings.

# String Concatenation: A good example of String concatenation has already been displayed when we
# added the strings 'firstName' and 'lastName' with a blank space ' ' in between to form
# the string 'fullName'.

# String Multiplication:
firstNameRepeated = firstName * 4;
print('First Name Repeated 4 Times: ' + firstNameRepeated + '\n');     # The output for the above statement is found to
                                                                # to be:
# First Name Repeated 4 Times: KevinKevinKevinKevin

# Sequence Operatrions on Strings: We've already witnessed how we can access characters in
# a String sequence at positions we desire. There are a few more fun sequence operations
# that can be used to work with Strings. Let's have a look at them.

# Characters in a String can also be fetched from the right side, and not just from the left.
# Like this:
print('Character at last position of Full Name: ' + fullName[-1]);
print('Character at second to last position of Full Name: ' + fullName[-2]);
print('Character at eight to last position of Full Name: ' + fullName[-8] + '\n');

# You can also access particlar lengths of characters within the String sequence. For example,
# if you want to access characters numbered 3 to 10 in String 'fullName':
print('Characters at position 3 to 10 in Full Name: ' + fullName[3:11] + '\n');    # The output for this line of code is: in Seque.
                                                                            # Look at the code carefully. If you want to access
# the characters fron X to Y, the code for that operation will be as follows: 'String[X:Y+1]'.

# This operation is called 'String Slicing' and turns out to be really important. But why?
# That's because Strings are Immutable Objects in Python. What's immutability?
# Immutability means that once an object has been assigned a value, it cannot be changed.
# Objects can either be mutable, or immutable. In Python, 'Numbers', 'Strings', and 'Tuples' (which we'll
# look into down the line) are immutable. All the other data types are mutable.

# Check this out:
print('Object ID: ' + str(id(firstName)));      # The output for this line is: Object ID: 24751936
firstName = 'Annet';                            # Here, we're assignign a new value to the variable 'firstName'
print('Object ID: ' + str(id(firstName)) + '\n');      # Now, the output is: Object ID: 24752000

# So basically, we see that when we give a new value to 'firstName', Python doesn't simply
# overwrite the previous value, but rather creates a new object with a new object ID.

del firstName;      # This command deletes any variables that have the name 'firstName'.

firstName = 'Kevin';    # Let's reassign a value 'Kevin' to a variable 'firstName'.

# So basically, how does 'slicing' Strings come to the rescue against immutability?
# Well, since you can't shorten, lengthen, or change the original characters of a String,
# you assign the sliced String characters and run operations and functions over them.
# For example, let's say I want to change the first (0th) character of the String 'firstName':
slicedFirstName_1 = 'T' + firstName[1:];
print('Sliced First Name Example 1: ' + slicedFirstName_1 + '\n');      # The output of the given two lines is:
                                                                        # Sliced First Name Example 1: Tevin.
# You see, the 0th character of the sliced firstName is added to 'T' to give 'Tevin'.
# Another interesting thing here is the syntax. 'firstName[1:0] takes us all the way from the first
# character at position '1' to the last character of the String. Let's look at a couple of other examples:
slicedFirstName_2 = firstName[:2] + 'ndrick';
print('Sliced First Name Example 2: ' + slicedFirstName_2 + '\n');      # The output here will be:
                                                                        # Sliced First Name Example 2: Kendrick ('Ke' + 'ndrick')

slicedFirstName_3 = 'N' + firstName[1:4] + 'lle';
print('Sliced First Name Example 2: ' + slicedFirstName_3 + '\n');      # The output for this will be:
                                                                        # Sliced First Name Example 3: Neville

# Apart from running operations on Strings, Python also provides us with it's own set of
# 'Type Specific Methods' that can be used to manipulate String content. No, don't get
# me wrong. You can't manipluate the original String, but you can store the manipulated
# String into another String variable. The most common String methods are 'find' and 'split'.

find_lastName = fullName.find('Sequeira');                  # The .find() method looks for the position where the first 
print('Last Name Found at position ' + str(find_lastName) + '\n');    # occurance of the String mentioned within the parenthesis is found.
                                                            # In this case, the String 'Sequeira' is found to begin from the 
# 6th position parent String 'fullName'.

find_e_in_fullName = fullName.find('e');        # This statement looks for the letter 'e' in the String 'fullName'.
print('Letter \'e\' found at position ' + str(find_e_in_fullName) + ' in Full Name' + '\n');    # Note that 'Kevin Sequeira' has
                                                                                                # three 'e's at different positions.
# But the statment fetches the position number where the first 'e' is found.

# Another thing to look at is 'Case Sensitivity' of String methods.
find_E_in_fullName = fullName.find('E');        # This statement looks for the letter 'E' in the String 'fullName', and doesn't
print('Letter \'E\' found at position ' + str(find_E_in_fullName) + ' in Full Name' + '\n');    # find it, as there is no
                                                                                                # upper case 'E' present in the
# String. When no result is found by the '.find()' method, it returns a '-1' as the output.

# Let's have a look at the '.split()' method:
keywords = 'Acquisition Editor / Engineer / Web Developer'
print('Keywords: ' + keywords + '\n');
list_keywords = keywords.split(' / ');      # The '.split()' method splits a String at those points which match the
print(str(list_keywords) + '\n');           # character mentioned within the parenthesis (space-forward slash-space, in this case).
                                            # The output of this code is:
# ['Acquisition Editor', 'Engineer', 'Web Developer']
# The String is basically split into a number of substrings and are saved as a 'List'.
# We'll look at what Lists are in a little while from now.

# There's another common method used with Strings, called '.replace()'. Just as the name suggests
# the function replaces that part of the String with another substring, and saves it as a separate object.
replacedFirstName_fullName = fullName.replace('Kevin', 'Diana');
print('Original Full Name: ' + fullName + '\n');
print('Full Name with Replaced First Name: ' + replacedFirstName_fullName + '\n');
# I believe the above example simply explains how the '.replace()' method replaces substrings within Strings.

# So, that's all about Strings for now. There're a few other concepts that I've left out for now.
# Unicode Strings, Byte Strings, these we shall look into at a little later stage in our tutorial. 
