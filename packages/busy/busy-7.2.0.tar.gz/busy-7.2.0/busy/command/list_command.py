from wizlib.parser import WizParser

from busy.command import CollectionCommand


class ListCommand(CollectionCommand):
    """Show the descriptions with selection numbers, default to all"""

    name = 'list'
    extended: bool = False
    default_filter = ['1-']
    FORMATS = {
        'description': "{!s}",
        'plan_date': "{:%Y-%m-%d}",
        'done_date': "{:%Y-%m-%d}"
    }

    @classmethod
    def add_args(cls, parser: WizParser):
        super().add_args(parser)
        parser.add_argument('--extended', '-x', action='store_true')

    @CollectionCommand.wrap
    def execute(self):
        def format(item, index):
            result = f"{(index+1):>6}"
            if self.extended:
                text = f"{item.elapsed_time_text}"
                result += f"  {text:>8}"
            for colname in self.collection.schema:
                format = self.FORMATS[colname]
                if (colname == 'description'):
                    value = item.listable
                else:
                    value = getattr(item, colname)
                result += f"  {format.format(value)}"
            return result
        self.status = f"Listed {self.summarize()}"
        return self.output_items(format, with_index=True)
