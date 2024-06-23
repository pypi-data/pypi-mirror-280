# URL Shortener Package
This package provides utility functions as well as views for shortening urls and redirecting to original urls.

### Installation

You can install this package using pip:
    
    ## required for reading env file

    pip install django-environ
	
	## migration file is included in the package.
    ## Need run following cmd to migrate

    python manage.py migrate

### Configuration

Setup env file:
    
    URLSHORT_SCHEME=http/https

    URLSHORT_DOMAIN=127.0.0.1:9000/your_endpoint
        specify the domain name for shortened url
        note: domain should include endpoint specified for urlshort.urls in settings.py
        
    URLSHORT_EXPIRES_AT=2
        specify the validity of url in days

Add the following in your project's settings.py file:
    
    ## add following lines if not present else ignore
    import environ
    env = environ.Env()
    environ.Env.read_env()
    
     ## add urlshort in INSTALLED_APPS
    INSTALLED_APPS = [
        ... ,
        'urlshort'
    ]
    
    If using .env file
    URLSHORT = {
        'URLSHORT_SCHEME': env('URLSHORT_SCHEME'),
        'URLSHORT_DOMAIN': env('URLSHORT_DOMAIN'),
        'EXPIRES_AT': env('URLSHORT_EXPIRES_AT')
    }

    If using secrets.json file
    URLSHORT = {
        'URLSHORT_SCHEME': get_secret('URLSHORT_SCHEME'),
        'URLSHORT_DOMAIN': get_secret('URLSHORT_DOMAIN'),
        'EXPIRES_AT': get_secret('URLSHORT_EXPIRES_AT')
    }

### Usage

Valid URL should always end with backlash: https://www.google.com/
Following URL will be considered invalid: http://www.google.com

#### Using views:

Add following in your project's urls.py file:
    
    urlpatterns = [
        ... ,
        path('your_endpoint/', include('urlshort.urls'))
    ]
    
##### shorten_url

    ENDPOINT = defined in urlpatterns for the package's urls

    POST request:
    
        curl --location 'your_server_domain/ENDPOINT/apis/url/create' \
        --data '{
            "original_url": "https://www.postgresql.org/docs/7.3/arrays.html"
        }

        for example:
            curl --location 'your_server_domain/your_endpoint/apis/url/create' \
            --data '{
                "original_url": "https://www.postgresql.org/docs/7.3/arrays.html"
            }

    SCHEME and DOMAIN = defined in your env/secrets file
    
    response:
        
        {
            "status": "01",
            "data": {
                "created_at": "2023-10-25T12:00:12.623Z",
                "original_url": "https://www.postgresql.org/docs/7.3/arrays.html",
                "short_url": "SCHEME://DOMAIN/ENDPOINT/CWmPYIc",
                "expires_at": "2023-10-26T12:00:12.621Z",
                "alias": "CWmPYIc",
                "domain": "DOMAIN",
                "is_active": true,
                "hit_count": 0
            }
        }


#### Using helper functions:

##### shorten url:
    
    original_url = "https://www.google.com/"
    
    from urlshort.helpers import shorten_url
    
    short_url = shorten_url(value)

##### get_original_url:

    note: get_original_url function takes in unique_id as argument:
        unqiue_id = Pq3E8yy
    
    from urlshort.helpers import get_original_url
    
    original_url = get_original_url(unique_id)

