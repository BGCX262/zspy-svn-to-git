def siteurl(url):
    return '/'.join(url.split('/',3)[:3])

def abs_href(href,url):
    if len(href):
        if('/'==href[0]):
            return siteurl(url)+href
        try:
            first=href.index('://')
            try:
                href.index('/',0,first)
            except ValueError:
                return href
        except ValueError:
            pass
        try:
            url=url[:url.rindex('/')]+'/'
        except ValueError:
            pass
        return url+href
    return url

def sitename(url):
    return url.split('/',3)[2]
