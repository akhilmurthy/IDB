@title[Title]
### <span style="font-family:Helvetica Neue; font-weight:bold"> <span style="color:#f99e1a">Overwatch</span>glamour.me</span>
Group 4

---
@title[Introduction]
### <span style="font-family:Helvetica Neue; font-weight:bold"> <span style="color:#f99e1a">Introduction</span></span>

![profile](static/media/gitpitch/akhil.png)
![profile](static/media/gitpitch/allen.png)
![profile](static/media/gitpitch/peter.png)
![profile](static/media/gitpitch/sangwon.png)

+++
@title[Akhil]

![profile](static/media/gitpitch/akhil.png)

![](static/media/gitpitch/akhil uml.png)
![](static/media/gitpitch/akhil report.png)
![](static/media/gitpitch/akhil planitpoker.png)
![](static/media/gitpitch/akhil db.png)

+++
@title[Allen]
![profile](static/media/gitpitch/allen.png)

![profile](static/media/gitpitch/allen apiary.png)
![profile](static/media/gitpitch/allen unit tests.png)
![profile](static/media/gitpitch/allen search.png)

+++
@title[Peter]
![profile](static/media/gitpitch/peter.png)

![profile](static/media/gitpitch/peter scraping.png)
![profile](static/media/gitpitch/peter parsing.png)
![profile](static/media/gitpitch/peter bot.png)
![profile](static/media/gitpitch/peter populate.png)

+++
@title[Sangwon]
![profile](static/media/gitpitch/sangwon.png)

![profile](static/media/gitpitch/sangwon front.png)
![profile](static/media/gitpitch/sangwon sortfilter.png)
![profile](static/media/gitpitch/sangwon api.png)

---
@title[Demonstration]
### <span style="font-family:Helvetica Neue; font-weight:bold"> <span style="color:#f99e1a">Demonstration</span></span>

 
<a target="_blank" href="https://overwatchglamour.me" style="color:white">Navigate</a></span>

<a target="_blank" href="https://overwatchglamour.me/search%3Fsearch_str%3Dthe%3Fcurrent_view%3DHero" style="color:white">Search</a></span>

<a style="color:white">Unit Tests</a>
 
---
@title[Self Critique]
### <span style="font-family:Helvetica Neue; font-weight:bold"> <span style="color:#f99e1a">Self Critique</span></span>
#### <a target="_blank" href="https://overwatchglamour.me" style="color:white">overwatchglamour.me</a></span>

+++
@title[What did we do well?]
### <span style="font-family:Helvetica Neue; font-weight:bold"> <span style="color:#f99e1a">What did we do well?</span></span>

- Asset Collection and Database Population
 - No Official API or asset sources
 - Multiple APIs and scrapers to gather, combine, reformat, and organize
- Team Cohesion and Organization
- Models are well connected

+++
@title[What did we learn?]
### <span style="font-family:Helvetica Neue; font-weight:bold"> <span style="color:#f99e1a">What did we learn?</span></span>

- Overwatch
- Being resourceful and adaptive to scrape for resources
- Task and issue tracking with Trello
- Github version control
- GCP is expensive

+++
@title[What can we do better?]
### <span style="font-family:Helvetica Neue; font-weight:bold"> <span style="color:#f99e1a">What can we do better?</span></span>

+++
@title[Instance Pages]
*Instance pages could have been more user friendly.*

<span style="color:#f99e1a">Solution: </span>Overlay data on the image instead of having to scroll past the image.

+++
@title[Hero Specific Filter]
*Finding things relating to a specific Hero could be easier for Achievements. Currently, hero-specific filters exist for all other models, but Achievements can only filter for hero association or no hero association*

<span style="color:#f99e1a">Solution: </span>Add the same drop down menu filter in the other models to Achievements, but include the existing options in the drop down menu as well.

+++
@title[Search bar UI]
*Search bar could be centered or more aesthetically placed.  Search algorithm could be improved.*

<span style="color:#f99e1a">Solution: </span>Nest the search bar into the nav bar.

+++
@title[Placeholder image]
*Website is slow*

<span style="color:#f99e1a">Solution: </span>Add caching to the website.

+++
@title[What puzzles us?]
### <span style="font-family:Helvetica Neue; font-weight:bold"> <span style="color:#f99e1a">What puzzles us?</span></span>

- Database connection
- React

---
@title[Other Critique]
### <span style="font-family:Helvetica Neue; font-weight:bold"> <span style="color:#f99e1a">Other Critique</span></span>
#### <a target="_blank" href="https://betterreads.me" style="color:white">betterreads.me</a></span>

+++
@title[What did they do well?]
### <span style="font-family:Helvetica Neue; font-weight:bold"> <span style="color:#f99e1a">What did they do well?</span></span>

- Aesthetic landing page and about page
- Nav bar highlights, 
- Page loads quickly and all at once
- They have a cool loading icon
- They implemented a search for each model

+++
@title[What did we learn from their website?]
### <span style="font-family:Helvetica Neue; font-weight:bold"> <span style="color:#f99e1a">What can we learn from their website?</span></span>

- The layout of the website could be much more interactive without sacrificing clarity and minimalism.
- J.K. Rowling has written other books apperently?

+++
@title[What can they do better?]
### <span style="font-family:Helvetica Neue; font-weight:bold"> <span style="color:#f99e1a">What can they do better?</span></span>

+++
@title[Missing Author and or Series]
### <span style="font-family:Helvetica Neue; font-weight:bold"> <span style="color:#f99e1a">Database connection issues</span></span>
Some books will have "No Series" and/or "No Author when not appropriate".

+++
@title[Review of a book lists incorrect author]
### <span style="font-family:Helvetica Neue; font-weight:bold"> <span style="color:#f99e1a">Reviews wrong book with wrong author</span></span>
Some reviews have the incorrect book being reviewed, but also the incorrect author of the incorrect book displayed. (Otis Chandler on Harry Potter #6; Author is Dale Peck)

+++
@title[Exact Search]
### <span style="font-family:Helvetica Neue; font-weight:bold"> <span style="color:#f99e1a">Exact Search</span></span>
The search finds exact matches by not omitting periods from the search. (J.K. Rowling)

+++
@title[Unclear/Inaccurate Filter Conditions]
### <span style="font-family:Helvetica Neue; font-weight:bold"> <span style="color:#f99e1a">Filters unclear or wrong</span></span>
When filtering by "Top Rated-",e.g. "Top Rated Books" , the criteria seems to be to filter out books with ratings lower than 4.2. 

The other two filters, "Series" and "Most Recent", are not actual filters, since they seem to still include books that are not in a series or just sort by how recent instead of filtering.

+++
@title[Filter and Sorting is disjoint]
### <span style="font-family:Helvetica Neue; font-weight:bold"> <span style="color:#f99e1a">Disjoint Filter and Sort</span></span>
It is not possible to sort and filter at the same time. Choosing one, overrides the other.

+++
@title[Book information on Reviews page]
### <span style="font-family:Helvetica Neue; font-weight:bold"> <span style="color:#f99e1a">Images in Reviews</span></span>
While the reviews tab has information on ratings, the reviewer's name, and date, it does not give information on the book being reviewed which would be very ueful for a user to know.


+++
@title[What puzzles us about their website?]
### <span style="font-family:Helvetica Neue; font-weight:bold"> <span style="color:#f99e1a">What puzzles us about their website?</span></span>

- The landing page carousel displays books can not be clicked.
- Why not have the first book's cover be the image for the Series Model instead of all placeholder images?
- Why their website has weird mistakes in their data, even though their API seems to have accurate data?



---
@title[Visualization]
### <span style="font-family:Helvetica Neue; font-weight:bold"> <span style="color:#f99e1a">Visualization</span></span>

<a target="_blank" href="http://overwatchglamour.me/visualization" style="color:white">Link</a></span>
