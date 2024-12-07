from pprint import pprint

def tokenize_file(filepath):
    # first, we have to prep the file data and strip a bit of whitespace
    #not all the whitespace tho, i'll be using the tabs and newlines as guides
    #for building the data structures
    container = [] #holds all of the lines
    removal_buffer = [] #temp variable for avoiding indexing errors

    with open(filepath,'r') as f:#open the file
        line_data = f.readline() #grab 0th line
        while line_data: #iterate through the file
            removal_buffer.append(line_data.replace('\n','')) #add lines to buffer
            line_data=f.readline()#move to next iteration

    while True: #idgaf, stop complaining
        if len(removal_buffer) > 0: #make sure the buffer has something in it
            if removal_buffer[0]!='': #make sure the string isnt empty
                if removal_buffer[0][0]!='#': #make sure it isnt a comment
                    container.append(removal_buffer[0]) #chuck it in the container
            removal_buffer.pop(0)#remove from buffer
        else:
            break #if the buffer is empty, break out of loop


    #now we need to find our breakpoints between variable name and its data.
    #or the class instance and its attributes
    #or the command and its arguments
    #i actually dont know how this data is parsed by the game 
    outfit_key_buffer = [] #the indexes for the outfit names will be here
    for i in range(0,len(container)):
        if container[i][:6]=='outfit': #this is our big alert flag.
            outfit_key_buffer.append(i)#log the index into key buffer

    outfits={}#this is one of our big bad evil variables.
    #oooooohh i know! i'll scope these by race to reduce variable size and make a lookup table!

    #time to actually add the data to the outfits dictionary
    for i in range(0,len(outfit_key_buffer)):
        idx = outfit_key_buffer[i] #this number will index the container for the key
        current_key = container[idx] #the line with the outfit key
        current_key = current_key.replace('outfit ','').replace('\"','')#make it purtty
        if i == len(outfit_key_buffer)-1:#last outfit first(otherwise shit breaks)
            outfits[current_key] = container[idx:]#add everything thru the end of the file
        else: #now we handle everything else.
            outfits[current_key] = container[idx+1:outfit_key_buffer[i+1]]

    #we have our keys set correctly, but our values are all fucked up
    #lets fix this
    for key in outfits.keys(): #iterate through outfits by key
        temp_container=outfits[key] #split the value into a list
        output_dict = {} #i will build this dictionary then copy it over the list in outfits
        for i in range(0,len(temp_container)):#index through temp container
            idx = temp_container[i] #grab a single attribute line
            #this block handles longer, multi-word values
            exceptions_list = [
                'description',
                'plural',
                'thumbnail',
                'category'
            ]
            for item in exceptions_list:#iterate through exceptions list by item
                if item in idx: #check if item is in the indexed line
                    output_dict[item] = ' '.join(idx.split()[1:]) #if so, handle it
                    break
            
                else: #notice how the string formatting is almost opposite to above
                    key_output = ' '.join(idx.split()[:-1]).replace('\"', '')#pretty up the key
                    if len(idx.split()) > 1:
                        value_output = idx.split()[-1]#pretty up the value
                    else:
                        value_output = idx
                    output_dict[key_output] = value_output
        outfits[key] = output_dict #push output to main variable

    #time to numerize the figures that are still strings
    for item in outfits: #iterate through outfits
        for attr in outfits[item]: #iterate through the outfit
            try: outfits[item][attr] = float(outfits[item][attr]) #attempt to convert the value to a float
            except ValueError: pass #if not, just move on

    print('file', filepath, "was loaded successfully")

#TODO: add exception handling since we are opening a metric fuckload of data here so there will probably
#be problems!


