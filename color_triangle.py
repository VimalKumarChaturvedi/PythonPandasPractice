def color_triangle(row):

    def return_3rd_color(two_letters):
        if two_letters in ('RG', 'GR'):
            return 'B'
        elif two_letters in ('RB', 'BR'):
            return 'G'
        else:
            return 'R'



    def print_next_line(current_word):
        current_length = (len(word_seq))
        return_word = ''

        for i in range(current_length-1):
            two_letters =  current_word[i:i+2] 
            if two_letters[0:1] == two_letters[1:2]:
                return_word += two_letters[0:1]
            else:
                return_word += return_3rd_color(two_letters)
        return return_word
            
    print(row)
    word_seq = row
    word_seq_lengtht = len(word_seq)
    for i in  range(word_seq_lengtht-1):
        word_seq= print_next_line(word_seq)
        print(word_seq)
    
color_triangle(None)