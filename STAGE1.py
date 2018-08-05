#DEFINING DATA-STRUCTURE
#DATA-TYPE=0
#ATTRIBUTE=1
#CONTROL=2
#OTHER=3
KEYWORDS_1=list(('char', 'double', 'enum', 'float', 'int', 'register', 'short', 'signed', 'union', 'unsigned', 'void', '*', 'struct'))
KEYWORDS_2=list(('const', 'extern', 'long', 'static', 'auto'))
KEYWORDS_3=list(('break', 'case', 'continue', 'default', 'do', 'else', 'for', 'for(', 'goto',  'if(', 'return', 'switch', 'switch(', 'while', 'while('))
KEYWORDS_4=list(('typedef', 'sizeof', 'volatile'))
IO_FUNC=list(('printf', 'scanf'))
#KEYWORDS=(('auto', 2), ('break', 3),	('case',3 ),	('char', 1),
#('const',2), 	('continue' ,3),	('default',3),	('do',3),
#('double',1),	('else',3),	('enum', 1),	 ('extern',2),
#('float', 1),	('for', 3),	('goto',3),	('if',3),
#('int', 1), 	('long', 2),	('register', 1),	('return',3),
#('short',1),	('signed',1),	('sizeof',4),	('static',2),
#('struct',2),	('switch',3),	('typedef',4),	('union',1),
#('unsigned', 1),	('void', 1),	 ('volatile',4),	('while',3));

#fp=open("text2.txt");
#Source Code
#SOURCE_CODE=fp.read();
#Types of Variables
#Number of Variables
#Return type of function Function
#Total number of functions
#Parameters to funtions
#Number of Keywords
class first(object):
    def __init__(self, fp):
        self.SOURCE_CODE=fp.read()
        self.types_of_variable=set();#done
        self.number_of_variables=0;#done
        self.name_of_variables=set();#done
        self.name_of_functions=set();#done
        self.number_of_functions=0;#done
        self.number_formal_variables=0;
        self.number_of_keywords=0;#done
        self.name_of_keywords=set();#done
        self.name_of_library=set();
        self.number_of_library=0;
        self.number_of_blankLines=0;
    def VariableFunction_Operator_Module(self,code):
        a=code.split()
        spinlock=False
        check_function_flag=False;    
        for words in a:
            #Checking for which category a keyword belongs
            p=words in KEYWORDS_1;
            x=words in KEYWORDS_2;
            y=words in KEYWORDS_3;
            z=words in KEYWORDS_4;
            #If its a library function
            if '<' and '>' in words:
                self.name_of_library.add(words);
                self.number_of_library+=1;
            #If its a blank line
            if words=='':
                self.number_of_blankLines+=1;
            #if its a keyword it must be among one the classes above
            if p or x or y or z:
                self.number_of_keywords=self.number_of_keywords+1;
                self.name_of_keywords.add(words);
            #Calculating number of formal variables
            if p:
                spinlock=True
                self.types_of_variable.add(words);
            if (words not in KEYWORDS_3) and ('(' in words or '()' in words):
                temp=words[0:words.find('(')]
                if temp not in IO_FUNC:
                    self.name_of_functions.add(temp)
                    check_function_flag=True;
            if check_function_flag and ')' in words:
                check_function_flag=False;
            if check_function_flag and words not in KEYWORDS_1:
                self.number_formal_variables=self.number_formal_variables+1;
            #Checking the names and number of vaoriables
            if spinlock and ';' in words:
                self.name_of_variables.add(words);
                self.number_of_variables=self.number_of_variables+1;
                spinlock=False;
            if spinlock and (',' in words or '=' in words) and not check_function_flag:
                if ',' in words:
                    words=words[0:words.find(',')]
                if '=' in words:
                    words=words[0:words.find('=')]
                if ';' in words:
                    words=words[0:words.find(';')]
                    print(words)
                if ',' in words and len(words)>2:
                    self.name_of_variables.add(words.split(','))
                    self.number_of_variables=self.number_of_variables+1;
                    self.name_of_variables.add(words);
        

    #Calculating th bind score from the data calculated using bind score heuristics
    def compute_bind(self):
        self.VariableFunction_Operator_Module(self.SOURCE_CODE)
        bind=0;
        bind=bind+(self.number_of_variables*1)
        bind=bind+(self.number_of_functions**2)#sqaure
        bind=bind+(self.number_formal_variables*4)
        bind=bind+(self.number_of_keywords*2)
        bind=bind+(self.number_of_blankLines*1)
        bind=bind+(self.number_of_library*1)
        
    
        return bind;
    

    


























