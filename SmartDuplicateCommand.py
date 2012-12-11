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

        def replace( match ):
            if ( match.group( 0 ) == ".height" ): return ".width"
            elif ( match.group( 0 ) == ".width" ): return ".height"
            elif ( match.group( 0 ) == ".x" ): return ".y"
            elif ( match.group( 0 ) == ".y" ): return ".x"

        string = re.sub( "(.height|.width|.x|.y)", replace, string )

        return string