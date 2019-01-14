from re import sub, escape

def regexStrip(text, char=" "):
    return sub('^['+escape(char)+']*|['+escape(char)+']*$', "", text)

print(regexStrip( "aaavawdafed advwavdaw cdvawaaa", "  " ))
