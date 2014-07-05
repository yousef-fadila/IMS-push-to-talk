### $ANTLR 2.7.6 (2005-12-22): "echarts.g" -> "echarts_l.py"$
### import antlr and other modules ..
import sys
import antlr

version = sys.version.split()[0]
if version < '2.2.1':
    False = 0
if version < '2.3':
    True = not False
### header action >>> 

### header action <<< 
### preamble action >>> 

### preamble action <<< 
### >>>The Literals<<<
literals = {}
literals[u"public"] = 83
literals[u"initial"] = 93
literals[u"new"] = 143
literals[u"implements"] = 80
literals[u"nonterminal"] = 94
literals[u"package"] = 74
literals[u"protected"] = 84
literals[u"machine"] = 77
literals[u"exit"] = 97
literals[u"transition"] = 101
literals[u"entry"] = 96
literals[u"final"] = 85
literals[u"delay"] = 109
literals[u"extends"] = 79
literals[u"private"] = 82
literals[u"static"] = 76
literals[u"abstract"] = 86
literals[u"concurrent"] = 95
literals[u"state"] = 89
literals[u"reflect"] = 100
literals[u"else"] = 104
literals[u"import"] = 75
literals[u"constport"] = 103


### import antlr.Token 
from antlr import Token
### >>>The Known Token Types <<<
SKIP                = antlr.SKIP
INVALID_TYPE        = antlr.INVALID_TYPE
EOF_TYPE            = antlr.EOF_TYPE
EOF                 = antlr.EOF
NULL_TREE_LOOKAHEAD = antlr.NULL_TREE_LOOKAHEAD
MIN_USER_TYPE       = antlr.MIN_USER_TYPE
BLOCK = 4
ACCESS_MODIFIERS = 5
OBJBLOCK = 6
MACHINE_BODY = 7
STATE_DEF = 8
TRANSITION_DEF = 9
ACTION_BLOCK = 10
HOST_BLOCK = 11
SRC_CONFIG = 12
TGT_CONFIG = 13
PORT_SEND = 14
EXPR = 15
PORT_REF = 16
PORT_RECEIVE = 17
GUARD = 18
COMPILATION_UNIT = 19
HOST = 20
IMPLEMENTS_CLAUSE = 21
STATE_MODIFIERS = 22
MACHINE_MODIFIERS = 23
EXTERNAL = 24
NO_SUBMACHINE = 25
STATES = 26
TRANSITIONS = 27
ENTRY = 28
EXIT = 29
INNER_SUBMACHINE = 30
EXTERNAL_SUBMACHINE = 31
VARIABLE_SUBMACHINE = 32
TRANSITION_ACTION = 33
BASIC_CONFIG = 34
VARIABLE_CONFIG = 35
DYNAMIC_CONFIG = 36
AND_CONFIG = 37
OR_CONFIG = 38
MULTI_CONFIG = 39
CONSTRUCTORS = 40
ARGUMENTS = 41
CONSTRUCTOR_DEF = 42
SET_INDEX = 43
GET_INDEX = 44
EMPTY_INDEX = 45
REFLECT_SUBMACHINE = 46
MACHINE_DEF = 47
TYPE = 48
ARRAY_INIT = 49
TRANSITION_MODIFIERS = 50
PARAMETERS = 51
PARAMETER_DEF = 52
IMPORT_DEF = 53
PACKAGE_DEF = 54
EXTENDS_CLAUSE = 55
ARRAY_DECLARATOR = 56
ELIST = 57
METHOD_CALL = 58
INDEX_OP = 59
TYPECAST = 60
NEW_EXPRESSION = 61
POST_DEC = 62
POST_INC = 63
UNARY_MINUS = 64
UNARY_PLUS = 65
PRIMARY_EXPRESSION = 66
COMPOUND_TGT = 67
BASIC_TGT = 68
GUARDED_TGT = 69
LINECOLUMN = 70
IMPORTS = 71
IMPORT_MODIFIERS = 72
SEMI = 73
LITERAL_package = 74
LITERAL_import = 75
LITERAL_static = 76
LITERAL_machine = 77
IDENT = 78
LITERAL_extends = 79
LITERAL_implements = 80
COMMA = 81
LITERAL_private = 82
LITERAL_public = 83
LITERAL_protected = 84
LITERAL_final = 85
LITERAL_abstract = 86
LCURLY = 87
RCURLY = 88
LITERAL_state = 89
COLON = 90
LBRACK = 91
RBRACK = 92
LITERAL_initial = 93
LITERAL_nonterminal = 94
LITERAL_concurrent = 95
LITERAL_entry = 96
LITERAL_exit = 97
LPAREN = 98
RPAREN = 99
LITERAL_reflect = 100
LITERAL_transition = 101
MINUS = 102
LITERAL_constport = 103
LITERAL_else = 104
DIV = 105
SMALL_ARROW = 106
DOT = 107
QUESTION = 108
LITERAL_delay = 109
STAR = 110
LNOT = 111
ASSIGN = 112
PLUS_ASSIGN = 113
MINUS_ASSIGN = 114
STAR_ASSIGN = 115
DIV_ASSIGN = 116
MOD_ASSIGN = 117
SR_ASSIGN = 118
BSR_ASSIGN = 119
SL_ASSIGN = 120
BAND_ASSIGN = 121
BXOR_ASSIGN = 122
BOR_ASSIGN = 123
LOR = 124
LAND = 125
BOR = 126
BXOR = 127
BAND = 128
NOT_EQUAL = 129
EQUAL = 130
LT = 131
GT = 132
LE = 133
GE = 134
SL = 135
SR = 136
BSR = 137
PLUS = 138
MOD = 139
INC = 140
DEC = 141
BNOT = 142
LITERAL_new = 143
NUM_INT = 144
CHAR_LITERAL = 145
STRING_LITERAL = 146
NUM_FLOAT = 147
NUM_LONG = 148
NUM_DOUBLE = 149
WS = 150
SL_COMMENT = 151
ML_COMMENT = 152
ESC = 153
HEX_DIGIT = 154
EXPONENT = 155
FLOAT_SUFFIX = 156

class Lexer(antlr.CharScanner) :
    ### user action >>>
    ### user action <<<
    def __init__(self, *argv, **kwargs) :
        antlr.CharScanner.__init__(self, *argv, **kwargs)
        self.caseSensitiveLiterals = True
        self.setCaseSensitive(True)
        self.literals = literals
    
    def nextToken(self):
        while True:
            try: ### try again ..
                while True:
                    _token = None
                    _ttype = INVALID_TYPE
                    self.resetText()
                    try: ## for char stream error handling
                        try: ##for lexical error handling
                            la1 = self.LA(1)
                            if False:
                                pass
                            elif la1 and la1 in u'?':
                                pass
                                self.mQUESTION(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'(':
                                pass
                                self.mLPAREN(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u')':
                                pass
                                self.mRPAREN(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'[':
                                pass
                                self.mLBRACK(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u']':
                                pass
                                self.mRBRACK(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'{':
                                pass
                                self.mLCURLY(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'}':
                                pass
                                self.mRCURLY(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u':':
                                pass
                                self.mCOLON(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u',':
                                pass
                                self.mCOMMA(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'~':
                                pass
                                self.mBNOT(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u';':
                                pass
                                self.mSEMI(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'\t\n\u000c\r ':
                                pass
                                self.mWS(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'\'':
                                pass
                                self.mCHAR_LITERAL(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'"':
                                pass
                                self.mSTRING_LITERAL(True)
                                theRetToken = self._returnToken
                            elif la1 and la1 in u'$ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz':
                                pass
                                self.mIDENT(True)
                                theRetToken = self._returnToken
                            else:
                                if (self.LA(1)==u'>') and (self.LA(2)==u'>') and (self.LA(3)==u'>') and (self.LA(4)==u'='):
                                    pass
                                    self.mBSR_ASSIGN(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'>') and (self.LA(2)==u'>') and (self.LA(3)==u'='):
                                    pass
                                    self.mSR_ASSIGN(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'>') and (self.LA(2)==u'>') and (self.LA(3)==u'>') and (True):
                                    pass
                                    self.mBSR(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'<') and (self.LA(2)==u'<') and (self.LA(3)==u'='):
                                    pass
                                    self.mSL_ASSIGN(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'=') and (self.LA(2)==u'='):
                                    pass
                                    self.mEQUAL(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'!') and (self.LA(2)==u'='):
                                    pass
                                    self.mNOT_EQUAL(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'/') and (self.LA(2)==u'='):
                                    pass
                                    self.mDIV_ASSIGN(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'+') and (self.LA(2)==u'='):
                                    pass
                                    self.mPLUS_ASSIGN(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'+') and (self.LA(2)==u'+'):
                                    pass
                                    self.mINC(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'-') and (self.LA(2)==u'='):
                                    pass
                                    self.mMINUS_ASSIGN(True)
                                    theRetToken = self._returnToken
                                elif ((self.LA(1)==u'-') and (self.LA(2)==u'-') and ( self.LA(3)!='>' )):
                                    pass
                                    self.mDEC(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'*') and (self.LA(2)==u'='):
                                    pass
                                    self.mSTAR_ASSIGN(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'%') and (self.LA(2)==u'='):
                                    pass
                                    self.mMOD_ASSIGN(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'>') and (self.LA(2)==u'>') and (True):
                                    pass
                                    self.mSR(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'>') and (self.LA(2)==u'='):
                                    pass
                                    self.mGE(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'<') and (self.LA(2)==u'<') and (True):
                                    pass
                                    self.mSL(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'<') and (self.LA(2)==u'='):
                                    pass
                                    self.mLE(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'^') and (self.LA(2)==u'='):
                                    pass
                                    self.mBXOR_ASSIGN(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'|') and (self.LA(2)==u'='):
                                    pass
                                    self.mBOR_ASSIGN(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'|') and (self.LA(2)==u'|'):
                                    pass
                                    self.mLOR(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'&') and (self.LA(2)==u'='):
                                    pass
                                    self.mBAND_ASSIGN(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'&') and (self.LA(2)==u'&'):
                                    pass
                                    self.mLAND(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'-') and (self.LA(2)==u'>'):
                                    pass
                                    self.mSMALL_ARROW(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'/') and (self.LA(2)==u'/'):
                                    pass
                                    self.mSL_COMMENT(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'/') and (self.LA(2)==u'*'):
                                    pass
                                    self.mML_COMMENT(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'<') and (self.LA(2)==u'*'):
                                    pass
                                    self.mHOST(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'.') and (True) and (True) and (True):
                                    pass
                                    self.mDOT(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'=') and (True):
                                    pass
                                    self.mASSIGN(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'!') and (True):
                                    pass
                                    self.mLNOT(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'/') and (True):
                                    pass
                                    self.mDIV(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'+') and (True):
                                    pass
                                    self.mPLUS(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'-') and (True):
                                    pass
                                    self.mMINUS(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'*') and (True):
                                    pass
                                    self.mSTAR(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'%') and (True):
                                    pass
                                    self.mMOD(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'>') and (True):
                                    pass
                                    self.mGT(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'<') and (True):
                                    pass
                                    self.mLT(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'^') and (True):
                                    pass
                                    self.mBXOR(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'|') and (True):
                                    pass
                                    self.mBOR(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'&') and (True):
                                    pass
                                    self.mBAND(True)
                                    theRetToken = self._returnToken
                                elif (self.LA(1)==u'.' or self.LA(1)==u'0' or self.LA(1)==u'1' or self.LA(1)==u'2' or self.LA(1)==u'3' or self.LA(1)==u'4' or self.LA(1)==u'5' or self.LA(1)==u'6' or self.LA(1)==u'7' or self.LA(1)==u'8' or self.LA(1)==u'9') and (True) and (True) and (True):
                                    pass
                                    self.mNUM_INT(True)
                                    theRetToken = self._returnToken
                                else:
                                    self.default(self.LA(1))
                                
                            if not self._returnToken:
                                raise antlr.TryAgain ### found SKIP token
                            ### return token to caller
                            return self._returnToken
                        ### handle lexical errors ....
                        except antlr.RecognitionException, e:
                            raise antlr.TokenStreamRecognitionException(e)
                    ### handle char stream errors ...
                    except antlr.CharStreamException,cse:
                        if isinstance(cse, antlr.CharStreamIOException):
                            raise antlr.TokenStreamIOException(cse.io)
                        else:
                            raise antlr.TokenStreamException(str(cse))
            except antlr.TryAgain:
                pass
        
    def mQUESTION(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = QUESTION
        _saveIndex = 0
        pass
        self.match('?')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mLPAREN(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = LPAREN
        _saveIndex = 0
        pass
        self.match('(')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mRPAREN(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = RPAREN
        _saveIndex = 0
        pass
        self.match(')')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mLBRACK(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = LBRACK
        _saveIndex = 0
        pass
        self.match('[')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mRBRACK(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = RBRACK
        _saveIndex = 0
        pass
        self.match(']')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mLCURLY(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = LCURLY
        _saveIndex = 0
        pass
        self.match('{')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mRCURLY(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = RCURLY
        _saveIndex = 0
        pass
        self.match('}')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mCOLON(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = COLON
        _saveIndex = 0
        pass
        self.match(':')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mCOMMA(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = COMMA
        _saveIndex = 0
        pass
        self.match(',')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mDOT(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = DOT
        _saveIndex = 0
        pass
        self.match('.')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mASSIGN(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = ASSIGN
        _saveIndex = 0
        pass
        self.match('=')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mEQUAL(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = EQUAL
        _saveIndex = 0
        pass
        self.match("==")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mLNOT(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = LNOT
        _saveIndex = 0
        pass
        self.match('!')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mBNOT(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = BNOT
        _saveIndex = 0
        pass
        self.match('~')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mNOT_EQUAL(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = NOT_EQUAL
        _saveIndex = 0
        pass
        self.match("!=")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mDIV(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = DIV
        _saveIndex = 0
        pass
        self.match('/')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mDIV_ASSIGN(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = DIV_ASSIGN
        _saveIndex = 0
        pass
        self.match("/=")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mPLUS(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = PLUS
        _saveIndex = 0
        pass
        self.match('+')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mPLUS_ASSIGN(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = PLUS_ASSIGN
        _saveIndex = 0
        pass
        self.match("+=")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mINC(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = INC
        _saveIndex = 0
        pass
        self.match("++")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mMINUS(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = MINUS
        _saveIndex = 0
        pass
        self.match('-')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mMINUS_ASSIGN(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = MINUS_ASSIGN
        _saveIndex = 0
        pass
        self.match("-=")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mDEC(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = DEC
        _saveIndex = 0
        if not  self.LA(3)!='>' :
            raise antlr.SemanticException(" self.LA(3)!='>' ")
        pass
        self.match("--")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mSTAR(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = STAR
        _saveIndex = 0
        pass
        self.match('*')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mSTAR_ASSIGN(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = STAR_ASSIGN
        _saveIndex = 0
        pass
        self.match("*=")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mMOD(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = MOD
        _saveIndex = 0
        pass
        self.match('%')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mMOD_ASSIGN(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = MOD_ASSIGN
        _saveIndex = 0
        pass
        self.match("%=")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mSR(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = SR
        _saveIndex = 0
        pass
        self.match(">>")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mSR_ASSIGN(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = SR_ASSIGN
        _saveIndex = 0
        pass
        self.match(">>=")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mBSR(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = BSR
        _saveIndex = 0
        pass
        self.match(">>>")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mBSR_ASSIGN(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = BSR_ASSIGN
        _saveIndex = 0
        pass
        self.match(">>>=")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mGE(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = GE
        _saveIndex = 0
        pass
        self.match(">=")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mGT(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = GT
        _saveIndex = 0
        pass
        self.match(">")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mSL(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = SL
        _saveIndex = 0
        pass
        self.match("<<")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mSL_ASSIGN(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = SL_ASSIGN
        _saveIndex = 0
        pass
        self.match("<<=")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mLE(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = LE
        _saveIndex = 0
        pass
        self.match("<=")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mLT(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = LT
        _saveIndex = 0
        pass
        self.match('<')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mBXOR(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = BXOR
        _saveIndex = 0
        pass
        self.match('^')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mBXOR_ASSIGN(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = BXOR_ASSIGN
        _saveIndex = 0
        pass
        self.match("^=")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mBOR(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = BOR
        _saveIndex = 0
        pass
        self.match('|')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mBOR_ASSIGN(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = BOR_ASSIGN
        _saveIndex = 0
        pass
        self.match("|=")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mLOR(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = LOR
        _saveIndex = 0
        pass
        self.match("||")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mBAND(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = BAND
        _saveIndex = 0
        pass
        self.match('&')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mBAND_ASSIGN(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = BAND_ASSIGN
        _saveIndex = 0
        pass
        self.match("&=")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mLAND(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = LAND
        _saveIndex = 0
        pass
        self.match("&&")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mSEMI(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = SEMI
        _saveIndex = 0
        pass
        self.match(';')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mSMALL_ARROW(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = SMALL_ARROW
        _saveIndex = 0
        pass
        self.match("->")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mWS(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = WS
        _saveIndex = 0
        pass
        _cnt258= 0
        while True:
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in u' ':
                pass
                self.match(' ')
            elif la1 and la1 in u'\t':
                pass
                self.match('\t')
            elif la1 and la1 in u'\u000c':
                pass
                self.match('\f')
            elif la1 and la1 in u'\n\r':
                pass
                if (self.LA(1)==u'\r') and (self.LA(2)==u'\n') and (True) and (True):
                    pass
                    self.match("\r\n")
                elif (self.LA(1)==u'\r') and (True) and (True) and (True):
                    pass
                    self.match('\r')
                elif (self.LA(1)==u'\n'):
                    pass
                    self.match('\n')
                else:
                    self.raise_NoViableAlt(self.LA(1))
                
                if not self.inputState.guessing:
                    self.newline()
            else:
                    break
                
            _cnt258 += 1
        if _cnt258 < 1:
            self.raise_NoViableAlt(self.LA(1))
        if not self.inputState.guessing:
            _ttype = SKIP
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mSL_COMMENT(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = SL_COMMENT
        _saveIndex = 0
        pass
        self.match("//")
        while True:
            if (_tokenSet_0.member(self.LA(1))):
                pass
                self.match(_tokenSet_0)
            else:
                break
            
        la1 = self.LA(1)
        if False:
            pass
        elif la1 and la1 in u'\n':
            pass
            self.match('\n')
        elif la1 and la1 in u'\r':
            pass
            self.match('\r')
            if (self.LA(1)==u'\n'):
                pass
                self.match('\n')
            else: ## <m4>
                    pass
                
        else:
            ##<m3> <closing
                pass
            
        if not self.inputState.guessing:
            _ttype = SKIP ; self.newline()
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mML_COMMENT(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = ML_COMMENT
        _saveIndex = 0
        pass
        self.match("/*")
        while True:
            if (self.LA(1)==u'\r') and (self.LA(2)==u'\n') and ((self.LA(3) >= u'\u0003' and self.LA(3) <= u'\u7ffe')) and ((self.LA(4) >= u'\u0003' and self.LA(4) <= u'\u7ffe')):
                pass
                self.match('\r')
                self.match('\n')
                if not self.inputState.guessing:
                    self.newline();
            elif ((self.LA(1)==u'*') and ((self.LA(2) >= u'\u0003' and self.LA(2) <= u'\u7ffe')) and ((self.LA(3) >= u'\u0003' and self.LA(3) <= u'\u7ffe')) and ( self.LA(2)!='/' )):
                pass
                self.match('*')
            elif (self.LA(1)==u'\r') and ((self.LA(2) >= u'\u0003' and self.LA(2) <= u'\u7ffe')) and ((self.LA(3) >= u'\u0003' and self.LA(3) <= u'\u7ffe')) and (True):
                pass
                self.match('\r')
                if not self.inputState.guessing:
                    self.newline();
            elif (self.LA(1)==u'\n'):
                pass
                self.match('\n')
                if not self.inputState.guessing:
                    self.newline();
            elif (_tokenSet_1.member(self.LA(1))):
                pass
                self.match(_tokenSet_1)
            else:
                break
            
        self.match("*/")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mCHAR_LITERAL(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = CHAR_LITERAL
        _saveIndex = 0
        pass
        self.match('\'')
        if (self.LA(1)==u'\\'):
            pass
            self.mESC(False)
        elif (_tokenSet_2.member(self.LA(1))):
            pass
            self.match(_tokenSet_2)
        else:
            self.raise_NoViableAlt(self.LA(1))
        
        self.match('\'')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mESC(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = ESC
        _saveIndex = 0
        pass
        self.match('\\')
        la1 = self.LA(1)
        if False:
            pass
        elif la1 and la1 in u'n':
            pass
            self.match('n')
        elif la1 and la1 in u'r':
            pass
            self.match('r')
        elif la1 and la1 in u't':
            pass
            self.match('t')
        elif la1 and la1 in u'b':
            pass
            self.match('b')
        elif la1 and la1 in u'f':
            pass
            self.match('f')
        elif la1 and la1 in u'"':
            pass
            self.match('"')
        elif la1 and la1 in u'\'':
            pass
            self.match('\'')
        elif la1 and la1 in u'\\':
            pass
            self.match('\\')
        elif la1 and la1 in u'u':
            pass
            _cnt279= 0
            while True:
                if (self.LA(1)==u'u'):
                    pass
                    self.match('u')
                else:
                    break
                
                _cnt279 += 1
            if _cnt279 < 1:
                self.raise_NoViableAlt(self.LA(1))
            self.mHEX_DIGIT(False)
            self.mHEX_DIGIT(False)
            self.mHEX_DIGIT(False)
            self.mHEX_DIGIT(False)
        elif la1 and la1 in u'0123':
            pass
            self.matchRange(u'0', u'3')
            if ((self.LA(1) >= u'0' and self.LA(1) <= u'7')) and (_tokenSet_0.member(self.LA(2))) and (True) and (True):
                pass
                self.matchRange(u'0', u'7')
                if ((self.LA(1) >= u'0' and self.LA(1) <= u'7')) and (_tokenSet_0.member(self.LA(2))) and (True) and (True):
                    pass
                    self.matchRange(u'0', u'7')
                elif (_tokenSet_0.member(self.LA(1))) and (True) and (True) and (True):
                    pass
                else:
                    self.raise_NoViableAlt(self.LA(1))
                
            elif (_tokenSet_0.member(self.LA(1))) and (True) and (True) and (True):
                pass
            else:
                self.raise_NoViableAlt(self.LA(1))
            
        elif la1 and la1 in u'4567':
            pass
            self.matchRange(u'4', u'7')
            if ((self.LA(1) >= u'0' and self.LA(1) <= u'7')) and (_tokenSet_0.member(self.LA(2))) and (True) and (True):
                pass
                self.matchRange(u'0', u'7')
            elif (_tokenSet_0.member(self.LA(1))) and (True) and (True) and (True):
                pass
            else:
                self.raise_NoViableAlt(self.LA(1))
            
        else:
                self.raise_NoViableAlt(self.LA(1))
            
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mSTRING_LITERAL(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = STRING_LITERAL
        _saveIndex = 0
        pass
        self.match('"')
        while True:
            if (self.LA(1)==u'\\'):
                pass
                self.mESC(False)
            elif (_tokenSet_3.member(self.LA(1))):
                pass
                self.match(_tokenSet_3)
            else:
                break
            
        self.match('"')
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mHEX_DIGIT(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = HEX_DIGIT
        _saveIndex = 0
        pass
        la1 = self.LA(1)
        if False:
            pass
        elif la1 and la1 in u'0123456789':
            pass
            self.matchRange(u'0', u'9')
        elif la1 and la1 in u'ABCDEF':
            pass
            self.matchRange(u'A', u'F')
        elif la1 and la1 in u'abcdef':
            pass
            self.matchRange(u'a', u'f')
        else:
                self.raise_NoViableAlt(self.LA(1))
            
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mIDENT(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = IDENT
        _saveIndex = 0
        pass
        la1 = self.LA(1)
        if False:
            pass
        elif la1 and la1 in u'abcdefghijklmnopqrstuvwxyz':
            pass
            self.matchRange(u'a', u'z')
        elif la1 and la1 in u'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            pass
            self.matchRange(u'A', u'Z')
        elif la1 and la1 in u'_':
            pass
            self.match('_')
        elif la1 and la1 in u'$':
            pass
            self.match('$')
        else:
                self.raise_NoViableAlt(self.LA(1))
            
        while True:
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in u'abcdefghijklmnopqrstuvwxyz':
                pass
                self.matchRange(u'a', u'z')
            elif la1 and la1 in u'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                pass
                self.matchRange(u'A', u'Z')
            elif la1 and la1 in u'_':
                pass
                self.match('_')
            elif la1 and la1 in u'0123456789':
                pass
                self.matchRange(u'0', u'9')
            elif la1 and la1 in u'$':
                pass
                self.match('$')
            else:
                    break
                
        ### option { testLiterals=true } 
        _ttype = self.testLiteralsTable(_ttype)
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mNUM_INT(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = NUM_INT
        _saveIndex = 0
        f1 = None
        f2 = None
        f3 = None
        f4 = None
        isDecimal = False
        t = None
        la1 = self.LA(1)
        if False:
            pass
        elif la1 and la1 in u'.':
            pass
            self.match('.')
            if not self.inputState.guessing:
                _ttype = DOT;
            if ((self.LA(1) >= u'0' and self.LA(1) <= u'9')):
                pass
                _cnt292= 0
                while True:
                    if ((self.LA(1) >= u'0' and self.LA(1) <= u'9')):
                        pass
                        self.matchRange(u'0', u'9')
                    else:
                        break
                    
                    _cnt292 += 1
                if _cnt292 < 1:
                    self.raise_NoViableAlt(self.LA(1))
                if (self.LA(1)==u'E' or self.LA(1)==u'e'):
                    pass
                    self.mEXPONENT(False)
                else: ## <m4>
                        pass
                    
                if (self.LA(1)==u'D' or self.LA(1)==u'F' or self.LA(1)==u'd' or self.LA(1)==u'f'):
                    pass
                    self.mFLOAT_SUFFIX(True)
                    f1 = self._returnToken
                    if not self.inputState.guessing:
                        t=f1
                else: ## <m4>
                        pass
                    
                if not self.inputState.guessing:
                    if t != None:
                       if 'F' in t.getText().upper():
                           _ttype = NUM_FLOAT
                       else:
                           _ttype = NUM_DOUBLE
            else: ## <m4>
                    pass
                
        elif la1 and la1 in u'0123456789':
            pass
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in u'0':
                pass
                self.match('0')
                if not self.inputState.guessing:
                    isDecimal = True;
                if (self.LA(1)==u'X' or self.LA(1)==u'x'):
                    pass
                    la1 = self.LA(1)
                    if False:
                        pass
                    elif la1 and la1 in u'x':
                        pass
                        self.match('x')
                    elif la1 and la1 in u'X':
                        pass
                        self.match('X')
                    else:
                            self.raise_NoViableAlt(self.LA(1))
                        
                    _cnt299= 0
                    while True:
                        if (_tokenSet_4.member(self.LA(1))) and (True) and (True) and (True):
                            pass
                            self.mHEX_DIGIT(False)
                        else:
                            break
                        
                        _cnt299 += 1
                    if _cnt299 < 1:
                        self.raise_NoViableAlt(self.LA(1))
                else:
                    synPredMatched304 = False
                    if ((self.LA(1) >= u'0' and self.LA(1) <= u'9')) and (True) and (True) and (True):
                        _m304 = self.mark()
                        synPredMatched304 = True
                        self.inputState.guessing += 1
                        try:
                            pass
                            _cnt302= 0
                            while True:
                                if ((self.LA(1) >= u'0' and self.LA(1) <= u'9')):
                                    pass
                                    self.matchRange(u'0', u'9')
                                else:
                                    break
                                
                                _cnt302 += 1
                            if _cnt302 < 1:
                                self.raise_NoViableAlt(self.LA(1))
                            la1 = self.LA(1)
                            if False:
                                pass
                            elif la1 and la1 in u'.':
                                pass
                                self.match('.')
                            elif la1 and la1 in u'Ee':
                                pass
                                self.mEXPONENT(False)
                            elif la1 and la1 in u'DFdf':
                                pass
                                self.mFLOAT_SUFFIX(False)
                            else:
                                    self.raise_NoViableAlt(self.LA(1))
                                
                        except antlr.RecognitionException, pe:
                            synPredMatched304 = False
                        self.rewind(_m304)
                        self.inputState.guessing -= 1
                    if synPredMatched304:
                        pass
                        _cnt306= 0
                        while True:
                            if ((self.LA(1) >= u'0' and self.LA(1) <= u'9')):
                                pass
                                self.matchRange(u'0', u'9')
                            else:
                                break
                            
                            _cnt306 += 1
                        if _cnt306 < 1:
                            self.raise_NoViableAlt(self.LA(1))
                    elif ((self.LA(1) >= u'0' and self.LA(1) <= u'7')) and (True) and (True) and (True):
                        pass
                        _cnt308= 0
                        while True:
                            if ((self.LA(1) >= u'0' and self.LA(1) <= u'7')):
                                pass
                                self.matchRange(u'0', u'7')
                            else:
                                break
                            
                            _cnt308 += 1
                        if _cnt308 < 1:
                            self.raise_NoViableAlt(self.LA(1))
                    else: ## <m4>
                            pass
                        
            elif la1 and la1 in u'123456789':
                pass
                pass
                self.matchRange(u'1', u'9')
                while True:
                    if ((self.LA(1) >= u'0' and self.LA(1) <= u'9')):
                        pass
                        self.matchRange(u'0', u'9')
                    else:
                        break
                    
                if not self.inputState.guessing:
                    isDecimal=True;
            else:
                    self.raise_NoViableAlt(self.LA(1))
                
            if (self.LA(1)==u'L' or self.LA(1)==u'l'):
                pass
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in u'l':
                    pass
                    self.match('l')
                elif la1 and la1 in u'L':
                    pass
                    self.match('L')
                else:
                        self.raise_NoViableAlt(self.LA(1))
                    
                if not self.inputState.guessing:
                    _ttype = NUM_LONG;
            elif ((self.LA(1)==u'.' or self.LA(1)==u'D' or self.LA(1)==u'E' or self.LA(1)==u'F' or self.LA(1)==u'd' or self.LA(1)==u'e' or self.LA(1)==u'f') and (isDecimal)):
                pass
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in u'.':
                    pass
                    self.match('.')
                    while True:
                        if ((self.LA(1) >= u'0' and self.LA(1) <= u'9')):
                            pass
                            self.matchRange(u'0', u'9')
                        else:
                            break
                        
                    if (self.LA(1)==u'E' or self.LA(1)==u'e'):
                        pass
                        self.mEXPONENT(False)
                    else: ## <m4>
                            pass
                        
                    if (self.LA(1)==u'D' or self.LA(1)==u'F' or self.LA(1)==u'd' or self.LA(1)==u'f'):
                        pass
                        self.mFLOAT_SUFFIX(True)
                        f2 = self._returnToken
                        if not self.inputState.guessing:
                            t=f2
                    else: ## <m4>
                            pass
                        
                elif la1 and la1 in u'Ee':
                    pass
                    self.mEXPONENT(False)
                    if (self.LA(1)==u'D' or self.LA(1)==u'F' or self.LA(1)==u'd' or self.LA(1)==u'f'):
                        pass
                        self.mFLOAT_SUFFIX(True)
                        f3 = self._returnToken
                        if not self.inputState.guessing:
                            t=f3
                    else: ## <m4>
                            pass
                        
                elif la1 and la1 in u'DFdf':
                    pass
                    self.mFLOAT_SUFFIX(True)
                    f4 = self._returnToken
                    if not self.inputState.guessing:
                        t=f4
                else:
                        self.raise_NoViableAlt(self.LA(1))
                    
                if not self.inputState.guessing:
                    if t != None:
                       if 'F' in t.getText().upper():
                           _ttype = NUM_FLOAT
                       else:
                           _ttype = NUM_DOUBLE
            else: ## <m4>
                    pass
                
        else:
                self.raise_NoViableAlt(self.LA(1))
            
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mEXPONENT(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = EXPONENT
        _saveIndex = 0
        pass
        la1 = self.LA(1)
        if False:
            pass
        elif la1 and la1 in u'e':
            pass
            self.match('e')
        elif la1 and la1 in u'E':
            pass
            self.match('E')
        else:
                self.raise_NoViableAlt(self.LA(1))
            
        la1 = self.LA(1)
        if False:
            pass
        elif la1 and la1 in u'+':
            pass
            self.match('+')
        elif la1 and la1 in u'-':
            pass
            self.match('-')
        elif la1 and la1 in u'0123456789':
            pass
        else:
                self.raise_NoViableAlt(self.LA(1))
            
        _cnt324= 0
        while True:
            if ((self.LA(1) >= u'0' and self.LA(1) <= u'9')):
                pass
                self.matchRange(u'0', u'9')
            else:
                break
            
            _cnt324 += 1
        if _cnt324 < 1:
            self.raise_NoViableAlt(self.LA(1))
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mFLOAT_SUFFIX(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = FLOAT_SUFFIX
        _saveIndex = 0
        la1 = self.LA(1)
        if False:
            pass
        elif la1 and la1 in u'f':
            pass
            self.match('f')
        elif la1 and la1 in u'F':
            pass
            self.match('F')
        elif la1 and la1 in u'd':
            pass
            self.match('d')
        elif la1 and la1 in u'D':
            pass
            self.match('D')
        else:
                self.raise_NoViableAlt(self.LA(1))
            
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    def mHOST(self, _createToken):    
        _ttype = 0
        _token = None
        _begin = self.text.length()
        _ttype = HOST
        _saveIndex = 0
        pass
        self.match("<*")
        while True:
            if (self.LA(1)==u'\r') and (self.LA(2)==u'\n') and ((self.LA(3) >= u'\u0003' and self.LA(3) <= u'\u7ffe')) and ((self.LA(4) >= u'\u0003' and self.LA(4) <= u'\u7ffe')):
                pass
                self.match('\r')
                self.match('\n')
                if not self.inputState.guessing:
                    self.newline();
            elif ((self.LA(1)==u'*') and ((self.LA(2) >= u'\u0003' and self.LA(2) <= u'\u7ffe')) and ((self.LA(3) >= u'\u0003' and self.LA(3) <= u'\u7ffe')) and ( self.LA(2)!='>' )):
                pass
                self.match('*')
            elif (self.LA(1)==u'\r') and ((self.LA(2) >= u'\u0003' and self.LA(2) <= u'\u7ffe')) and ((self.LA(3) >= u'\u0003' and self.LA(3) <= u'\u7ffe')) and (True):
                pass
                self.match('\r')
                if not self.inputState.guessing:
                    self.newline();
            elif (self.LA(1)==u'\n'):
                pass
                self.match('\n')
                if not self.inputState.guessing:
                    self.newline();
            elif (_tokenSet_1.member(self.LA(1))):
                pass
                self.match(_tokenSet_1)
            else:
                break
            
        self.match("*>")
        self.set_return_token(_createToken, _token, _ttype, _begin)
    
    

### generate bit set
def mk_tokenSet_0(): 
    data = [0L] * 1024 ### init list
    data[0] =-9224L
    for x in xrange(1, 511):
        data[x] = -1L
    data[511] =9223372036854775807L
    return data
_tokenSet_0 = antlr.BitSet(mk_tokenSet_0())

### generate bit set
def mk_tokenSet_1(): 
    data = [0L] * 1024 ### init list
    data[0] =-4398046520328L
    for x in xrange(1, 511):
        data[x] = -1L
    data[511] =9223372036854775807L
    return data
_tokenSet_1 = antlr.BitSet(mk_tokenSet_1())

### generate bit set
def mk_tokenSet_2(): 
    data = [0L] * 1024 ### init list
    data[0] =-549755823112L
    data[1] =-268435457L
    for x in xrange(2, 511):
        data[x] = -1L
    data[511] =9223372036854775807L
    return data
_tokenSet_2 = antlr.BitSet(mk_tokenSet_2())

### generate bit set
def mk_tokenSet_3(): 
    data = [0L] * 1024 ### init list
    data[0] =-17179878408L
    data[1] =-268435457L
    for x in xrange(2, 511):
        data[x] = -1L
    data[511] =9223372036854775807L
    return data
_tokenSet_3 = antlr.BitSet(mk_tokenSet_3())

### generate bit set
def mk_tokenSet_4(): 
    data = [0L] * 513 ### init list
    data[0] =287948901175001088L
    data[1] =541165879422L
    return data
_tokenSet_4 = antlr.BitSet(mk_tokenSet_4())
    
### __main__ header action >>> 
if __name__ == '__main__' :
    import sys
    import antlr
    import echarts_l
    
    ### create lexer - shall read from stdin
    try:
        for token in echarts_l.Lexer():
            print token
            
    except antlr.TokenStreamException, e:
        print "error: exception caught while lexing: ", e
### __main__ header action <<< 
