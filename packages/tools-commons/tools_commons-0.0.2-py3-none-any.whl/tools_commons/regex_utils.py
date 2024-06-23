def regex_or(*items):
    return "(?:" + "|".join(items) + ")"


punct_chars = r"['\"" "''.?!…,:;]"
punct_seq = r"['\"" "'']+|[.?!,…]+|[:;]+"  # 'anthem'. => ' anthem ' .
entity = r"[&<>\"]"
url_start_1 = r"(?:https?://|\bwww\.)"
commonTLDs = r"(?:com|org|edu|gov|net|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|pro|tel|travel|xxx)"
cc_tlds = (
    r"(?:ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|"
    r"bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|"
    r"er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|"
    r"hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|"
    r"lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|"
    r"nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|sk|"
    r"sl|sm|sn|so|sr|ss|st|su|sv|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|"
    r"va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|za|zm|zw)"
)  # TODO: remove obscure country domains?
url_start_2 = (
    r"\b(?:[A-Za-z\d-])+(?:\.[A-Za-z0-9]+){0,3}\."
    + regex_or(commonTLDs, cc_tlds)
    + r"(?:\."
    + cc_tlds
    + r")?(?=\W|$)"
)
url_body = r"(?:[^\.\s<>][^\s<>]*?)?"
url_extra_crap_before_end = regex_or(punct_chars, entity) + "+?"
url_end = r"(?:\.\.+|[<>]|\s|$)"
URL_REGEX = (
    regex_or(url_start_1, url_start_2)
    + url_body
    + "(?=(?:"
    + url_extra_crap_before_end
    + ")?"
    + url_end
    + ")"
)

punct_regex = r"[#@!?.:;,\'\"(\[)\]]"
space_regex = r" +"
newline_regex = r"\n+"
