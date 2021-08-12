# Generated from AFM.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("[\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\7\3\31\n\3\f\3\16")
        buf.write("\3\34\13\3\3\4\3\4\3\4\5\4!\n\4\3\4\3\4\3\5\5\5&\n\5\3")
        buf.write("\5\3\5\5\5*\n\5\3\5\3\5\5\5.\n\5\3\6\5\6\61\n\6\3\6\3")
        buf.write("\6\5\6\65\n\6\3\7\5\78\n\7\3\7\3\7\3\7\3\7\5\7>\n\7\3")
        buf.write("\b\3\b\6\bB\n\b\r\b\16\bC\3\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\5\nM\n\n\3\n\3\n\5\nQ\n\n\3\n\3\n\6\nU\n\n\r\n\16\nV")
        buf.write("\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\2\2_\2\24\3")
        buf.write("\2\2\2\4\26\3\2\2\2\6\35\3\2\2\2\b%\3\2\2\2\n\60\3\2\2")
        buf.write("\2\f\67\3\2\2\2\16A\3\2\2\2\20E\3\2\2\2\22L\3\2\2\2\24")
        buf.write("\25\5\4\3\2\25\3\3\2\2\2\26\32\7\3\2\2\27\31\5\6\4\2\30")
        buf.write("\27\3\2\2\2\31\34\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2")
        buf.write("\33\5\3\2\2\2\34\32\3\2\2\2\35 \5\b\5\2\36!\5\16\b\2\37")
        buf.write("!\5\22\n\2 \36\3\2\2\2 \37\3\2\2\2!\"\3\2\2\2\"#\7\4\2")
        buf.write("\2#\7\3\2\2\2$&\7\r\2\2%$\3\2\2\2%&\3\2\2\2&\'\3\2\2\2")
        buf.write("\')\7\13\2\2(*\7\r\2\2)(\3\2\2\2)*\3\2\2\2*+\3\2\2\2+")
        buf.write("-\7\5\2\2,.\7\r\2\2-,\3\2\2\2-.\3\2\2\2.\t\3\2\2\2/\61")
        buf.write("\7\r\2\2\60/\3\2\2\2\60\61\3\2\2\2\61\62\3\2\2\2\62\64")
        buf.write("\7\13\2\2\63\65\7\r\2\2\64\63\3\2\2\2\64\65\3\2\2\2\65")
        buf.write("\13\3\2\2\2\668\7\r\2\2\67\66\3\2\2\2\678\3\2\2\289\3")
        buf.write("\2\2\29:\7\6\2\2:;\7\13\2\2;=\7\7\2\2<>\7\r\2\2=<\3\2")
        buf.write("\2\2=>\3\2\2\2>\r\3\2\2\2?B\5\n\6\2@B\5\f\7\2A?\3\2\2")
        buf.write("\2A@\3\2\2\2BC\3\2\2\2CA\3\2\2\2CD\3\2\2\2D\17\3\2\2\2")
        buf.write("EF\7\6\2\2FG\7\f\2\2GH\7\b\2\2HI\7\f\2\2IJ\7\7\2\2J\21")
        buf.write("\3\2\2\2KM\7\r\2\2LK\3\2\2\2LM\3\2\2\2MN\3\2\2\2NP\5\20")
        buf.write("\t\2OQ\7\r\2\2PO\3\2\2\2PQ\3\2\2\2QR\3\2\2\2RT\7\t\2\2")
        buf.write("SU\5\n\6\2TS\3\2\2\2UV\3\2\2\2VT\3\2\2\2VW\3\2\2\2WX\3")
        buf.write("\2\2\2XY\7\n\2\2Y\23\3\2\2\2\20\32 %)-\60\64\67=ACLPV")
        return buf.getvalue()


class AFMParser ( Parser ):

    grammarFileName = "AFM.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'%Relationships'", "';'", "':'", "'['", 
                     "']'", "','", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "FEATURE", "INT", "SPACE", "WS" ]

    RULE_feature_model = 0
    RULE_relationships_block = 1
    RULE_relationship_spec = 2
    RULE_init_spec = 3
    RULE_obligatory_spec = 4
    RULE_optional_spec = 5
    RULE_non_cardinal_spec = 6
    RULE_cardinality = 7
    RULE_cardinal_spec = 8

    ruleNames =  [ "feature_model", "relationships_block", "relationship_spec", 
                   "init_spec", "obligatory_spec", "optional_spec", "non_cardinal_spec", 
                   "cardinality", "cardinal_spec" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    FEATURE=9
    INT=10
    SPACE=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Feature_modelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationships_block(self):
            return self.getTypedRuleContext(AFMParser.Relationships_blockContext,0)


        def getRuleIndex(self):
            return AFMParser.RULE_feature_model




    def feature_model(self):

        localctx = AFMParser.Feature_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_feature_model)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.relationships_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relationships_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationship_spec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AFMParser.Relationship_specContext)
            else:
                return self.getTypedRuleContext(AFMParser.Relationship_specContext,i)


        def getRuleIndex(self):
            return AFMParser.RULE_relationships_block




    def relationships_block(self):

        localctx = AFMParser.Relationships_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_relationships_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(AFMParser.T__0)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AFMParser.FEATURE or _la==AFMParser.SPACE:
                self.state = 21
                self.relationship_spec()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relationship_specContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def init_spec(self):
            return self.getTypedRuleContext(AFMParser.Init_specContext,0)


        def non_cardinal_spec(self):
            return self.getTypedRuleContext(AFMParser.Non_cardinal_specContext,0)


        def cardinal_spec(self):
            return self.getTypedRuleContext(AFMParser.Cardinal_specContext,0)


        def getRuleIndex(self):
            return AFMParser.RULE_relationship_spec




    def relationship_spec(self):

        localctx = AFMParser.Relationship_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_relationship_spec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.init_spec()
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 28
                self.non_cardinal_spec()
                pass

            elif la_ == 2:
                self.state = 29
                self.cardinal_spec()
                pass


            self.state = 32
            self.match(AFMParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_specContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FEATURE(self):
            return self.getToken(AFMParser.FEATURE, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(AFMParser.SPACE)
            else:
                return self.getToken(AFMParser.SPACE, i)

        def getRuleIndex(self):
            return AFMParser.RULE_init_spec




    def init_spec(self):

        localctx = AFMParser.Init_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_init_spec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AFMParser.SPACE:
                self.state = 34
                self.match(AFMParser.SPACE)


            self.state = 37
            self.match(AFMParser.FEATURE)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AFMParser.SPACE:
                self.state = 38
                self.match(AFMParser.SPACE)


            self.state = 41
            self.match(AFMParser.T__2)
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 42
                self.match(AFMParser.SPACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Obligatory_specContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FEATURE(self):
            return self.getToken(AFMParser.FEATURE, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(AFMParser.SPACE)
            else:
                return self.getToken(AFMParser.SPACE, i)

        def getRuleIndex(self):
            return AFMParser.RULE_obligatory_spec




    def obligatory_spec(self):

        localctx = AFMParser.Obligatory_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_obligatory_spec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AFMParser.SPACE:
                self.state = 45
                self.match(AFMParser.SPACE)


            self.state = 48
            self.match(AFMParser.FEATURE)
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 49
                self.match(AFMParser.SPACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_specContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FEATURE(self):
            return self.getToken(AFMParser.FEATURE, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(AFMParser.SPACE)
            else:
                return self.getToken(AFMParser.SPACE, i)

        def getRuleIndex(self):
            return AFMParser.RULE_optional_spec




    def optional_spec(self):

        localctx = AFMParser.Optional_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_optional_spec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AFMParser.SPACE:
                self.state = 52
                self.match(AFMParser.SPACE)


            self.state = 55
            self.match(AFMParser.T__3)
            self.state = 56
            self.match(AFMParser.FEATURE)
            self.state = 57
            self.match(AFMParser.T__4)
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 58
                self.match(AFMParser.SPACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_cardinal_specContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def obligatory_spec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AFMParser.Obligatory_specContext)
            else:
                return self.getTypedRuleContext(AFMParser.Obligatory_specContext,i)


        def optional_spec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AFMParser.Optional_specContext)
            else:
                return self.getTypedRuleContext(AFMParser.Optional_specContext,i)


        def getRuleIndex(self):
            return AFMParser.RULE_non_cardinal_spec




    def non_cardinal_spec(self):

        localctx = AFMParser.Non_cardinal_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_non_cardinal_spec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 63
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 61
                    self.obligatory_spec()
                    pass

                elif la_ == 2:
                    self.state = 62
                    self.optional_spec()
                    pass


                self.state = 65 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AFMParser.T__3) | (1 << AFMParser.FEATURE) | (1 << AFMParser.SPACE))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CardinalityContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(AFMParser.INT)
            else:
                return self.getToken(AFMParser.INT, i)

        def getRuleIndex(self):
            return AFMParser.RULE_cardinality




    def cardinality(self):

        localctx = AFMParser.CardinalityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cardinality)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(AFMParser.T__3)
            self.state = 68
            self.match(AFMParser.INT)
            self.state = 69
            self.match(AFMParser.T__5)
            self.state = 70
            self.match(AFMParser.INT)
            self.state = 71
            self.match(AFMParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cardinal_specContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cardinality(self):
            return self.getTypedRuleContext(AFMParser.CardinalityContext,0)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(AFMParser.SPACE)
            else:
                return self.getToken(AFMParser.SPACE, i)

        def obligatory_spec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AFMParser.Obligatory_specContext)
            else:
                return self.getTypedRuleContext(AFMParser.Obligatory_specContext,i)


        def getRuleIndex(self):
            return AFMParser.RULE_cardinal_spec




    def cardinal_spec(self):

        localctx = AFMParser.Cardinal_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cardinal_spec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AFMParser.SPACE:
                self.state = 73
                self.match(AFMParser.SPACE)


            self.state = 76
            self.cardinality()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AFMParser.SPACE:
                self.state = 77
                self.match(AFMParser.SPACE)


            self.state = 80
            self.match(AFMParser.T__6)
            self.state = 82 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 81
                self.obligatory_spec()
                self.state = 84 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AFMParser.FEATURE or _la==AFMParser.SPACE):
                    break

            self.state = 86
            self.match(AFMParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





