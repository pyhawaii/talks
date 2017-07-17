Read in the XML file: [records.xml](records.xml). This XML file has a structure that looks like this:

```xml
<records>
    <record>
        <datetime>2017-07-15 15:52:58.318527</datetime>
        <ipaddresses>
            <fmip>64.28.48.212</fmip>
            <toip>222.158.177.74</toip>
        </ipaddresses>
        <payload>819767</payload>
        <user id="customer">
            <fname>hal</fname>
            <lname>jordan</lname>
            <email>hjordan@jleague.org</email>
        </user>
    </record>
    ...
</records>
```

This puzzle has several components, with substeps. Complete as many as you can...

0) Find all records with dates in the year 2013
    * Display the date from the first record in that year
    * Display the date from the last record of that year
    * From just the 2013 records:
        * Display the last names of all users with an `id` attribute of `admin`

1) **Starting over with all the records**, this time, find all records with
    * A `payload` between `59500` and `60500`:
        * Display **all** the payloads that meet this criteria
    * For records with these payloads:
        * Display **all** the `toip` OR `fmip` IP addresses that fall within
          a `48.0.0.0/5` network.
