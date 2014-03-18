import sublime, sublime_plugin, re

class SmartDuplicateCommand( sublime_plugin.TextCommand ):

    def run( self, edit ):
        for region in self.view.sel():

            if region.empty():

                line = self.view.line( region )
                line_contents = self.scan( '\n' + self.view.substr( line ) )

                self.view.insert( edit, line.end(), line_contents )

            else:
                self.view.insert( edit, region.begin(), self.view.substr( region ) )

    def scan( self, string ):

        def hardReplace( match ):
            if ( match.group( 0 ) == ".x" ): return ".y"
            elif ( match.group( 0 ) == ".y" ): return ".x"

        def fillReplace( match ):
            value = match.group( 0 )

            if ( re.match( r"\w+X", value ) ): return value[ 0 : -1 ] + "Y"
            if ( re.match( r"\w+Y", value ) ): return value[ 0 : -1 ] + "X"

        def softReplace( match ):
            value = match.group( 0 )

            if ( value.istitle() ): transform = lambda string: string.title();
            elif ( value.isupper() ): transform = lambda string: string.upper();
            elif ( value.islower() ): transform = lambda string: string.lower();
            else: transform = lambda string: string

            value = value.lower();

            if ( value == "height" ): return transform( "width" )
            elif ( value == "width" ): return transform( "height" )
            elif ( value == "left" ): return transform( "right" )
            elif ( value == "right" ): return transform( "left" )
            elif ( value == "top" ): return transform( "bottom" )
            elif ( value == "bottom" ): return transform( "top" )

        string = re.sub( r"(\.x|\.y)", hardReplace, string )
        string = re.sub( r"(?i)(width|height|left|right|top|bottom)", softReplace, string )
        string = re.sub( r"(\w+X|\w+Y)", fillReplace, string )

        return string