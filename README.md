## Overscripted Web: A Mozilla Data Analysis Challenge
### How to participate

The Systems Research Group at Mozilla have created and open sourced a data set of publicly available information that was collected by a November 2017 Web crawl. We want to empower the community to explore the unseen or otherwise not obvious series of JavaScript execution events that are triggered once a user visits a webpage, and all the first- and third-party events that are set in motion when people retrieve content.

This is an exploratory data analysis. challenge. Mozilla would like to encourage participants to think outside the proverbial box, get creative, get under the surface. We want participants to analyze the data and come up with exciting new observations, patterns, research findings fitting into one of the following three categories:

- Tracking and Privacy
- Web Technologies and the Shape of the Modern Web
- Equality, Neutrality, and Law

The type of insights that we are looking for are illustrated in this [blog post](https://medium.com/firefox-context-graph/overscripted-digging-into-javascript-execution-at-scale-2ed508f21862). 

You can find the data set and everything you need to get started in the sections below.

### Technical criteria for submissions
- Analyses should be performed in Python using the [jupyter scientific notebook](https://jupyter-notebook.readthedocs.io/en/stable/) format and executing in this [environment](https://github.com/mozilla/Overscripted-Data-Analysis-Challenge/blob/master/analyses/environment.yaml). 
- Analysis can be submitted by filing a [Pull Request](https://help.github.com/articles/using-pull-requests) against __this__[ repository](https://github.com/mozilla/Overscripted-Data-Analysis-Challenge) with the analysis formatted as an *.ipynb file in the /analyses/ folder. 
  - Environment can be confugured locally by calling `conda env create -f  environment.yaml`
- Only *.ipynb format entries submitted via a pull request to the /analyses/ folder will be considered. Notebooks must be well documented and run on the [environment](https://github.com/mozilla/Overscripted-Data-Analysis-Challenge/blob/master/analyses/environment.yaml) described. Any entries not meeting these criteria will not be considered and no review will be carried out for error-generating code.
- Any additional code submitted will not be considered. The *.ipynb notebook should be a self contained analysis.

### Judging criteria
Analyses submitted for this challenge will be judged on the following attributes. More details area available in the __Official Challenge Rules__ included below.
#### Rigorous scientific approach
Submissions will be evaluated based on adherence to scientific method. Intermediate assumptions should be validated and supporting evidence referenced to where results are interpreted.
#### Alignment with Mozilla’s 10 founding principles
Submissions’ main finding is relevant to one of the 10 founding principles. 
#### Relevance
Analysis clearly shows or targets one or more of the three categories of the challenge: 
- Tracking and Privacy
- Web Technologies and the Shape of the Modern Web
- Equality, Neutrality and Law
#### Creativity 
submission demonstrates an innovative approach to data analysis and uncovers patterns in the data set that are not superficially obvious.

### Prizes
We will choose one winner from each of the three analysis categories:
- Tracking and Privacy
- Web Technologies and the Shape of the Modern Web
- Equality, Neutrality, and Law

Mozilla may even choose to invite winning teams to present their findings in a 15-minute talk at MozFest, though that is subject to change and to the particular entries and teams. MozFest is the world's leading festival for the open internet movement and takes place in London from October 26th to the 28th, 2018.

### Timeline
- June 4th, 2018: Contest launches
- August 31st, 2018: Submission deadline
- August 31st to September 13th, 2018: Judging period
- September 14th, 2018: Winners announcement
- October 26th to 28th, 2018: Session at MozFest

### Accessing the Data
Each of the links below links to a bz2 zipped portion of the total dataset. A small sample of the data is available in `safe_dataset.sample.tar.bz2` to get a feel for the content without commiting to the full download.
- [https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.sample.tar.bz2](https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.sample.tar.bz2)

Unzipped the full parquet data will be approximately 70Gb. Each (compressed) chunk dataset is around 9GB. `SHA256SUMS` contains the checksums for all datasets including the sample.
- [https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.0.tar.bz2](https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.0.tar.bz2)
- [https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.1.tar.bz2](https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.1.tar.bz2)
- [https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.2.tar.bz2](https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.2.tar.bz2)
- [https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.3.tar.bz2](https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.3.tar.bz2)
- [https://public-data.telemetry.mozilla.org/bigcrawl/SHA256SUMS](https://public-data.telemetry.mozilla.org/bigcrawl/SHA256SUMS)

### Official Challenge Rules
Overscripted Web: A Mozilla Data Analysis Challenge 
Official Rules
#### 1.    Sponsor.  
Sponsor of this Promotion is Mozilla Corporation, 331 E. Evelyn Avenue, Mountain View, CA, 94041.
 
#### 2.    No Purchase Necessary; Entry Instructions.  
NO PURCHASE OR PAYMENT OF ANY MONEY IS NECESSARY TO ENTER.  A PURCHASE WILL NOT IMPROVE THE CHANCES OF WINNING.  This is a contest of skill.  Odds of winning the Promotion depend on the number and quality of eligible entries received during the Promotion Period.  VOID WHERE PROHIBITED AND WHERE ANY REGISTRATION, BONDING, OR LOCALIZATION REQUIRED.
 
To enter the Promotion you must:
A. perform an analysis on the public dataset available here in Python using the jupyter scientific notebook format as a *.ipynb file,
B. Submit the entry to us by filing a [Pull Request against](https://help.github.com/articles/creating-a-pull-request/) the parent repository in the /analyses/ folder, available [here](https://github.com/mozilla/Overscripted-Data-Analysis-Challenge), including your name and Github username for communications about this Promotion. 
 
All requested entry information must be provided.  Further eligibility requirements are set forth below.
 
An Entrant may only submit one entry, and any attempt by any participant to obtain more than the stated number of entries by using multiple/different emails addresses, accounts, identities, or any other methods will void that participant's entries and that participant may be disqualified. Use of any automated system to participate is prohibited and will result in disqualification. In the event of a dispute as to any Entrant, the authorized account holder of the email address or other account associated with the entry will be deemed to be the Entrant. The “authorized account holder” is the natural person assigned an email address or other account by an Internet access provider, online service provider or other organization responsible for assigning email addresses or other online accounts for the domain associated with the submitted address. Each potential winner may be required to show proof of being the authorized account holder. In the event of an ongoing dispute as to any Entrant, Sponsor has the right to make a determination as to Entrant in its sole discretion.
 
You may enter as an individual or as part of a Team. For purposes of these Official Rules, a “Team” is defined as a group of individuals entering the Promotion jointly as one Entrant. Teams may have no more than 3 members.  By submitting your entry, either as an individual or as part of a Team, you are agreeing to these Official Rules. A Team will collectively also be deemed an Entrant.  Your entry submission information must include (i) your name and email address or preferred contact information, and (ii), if applicable, the names of all Team members.  

For any Team submission, the Team must agree to and designate one person as the agent of the Team to submit the entry and to accept the prize on behalf of the Team. Each individual on a Team must agree to these Official Rules. You may not make changes to your Team once registered to participate.  A Team will collectively be considered an Entrant. By submitting an entry, the submitter represents that all Team members have read and agreed to these Official Rules.
 
All entries must meet the following criteria:
 
- An entry shall consist of a *.ipynb file in Python using the jupyter scientific notebook format.
- The entry must clearly state which of the three categories the Entrant is submitting its entry to.
- Notebooks must be well documented and run on the environment described in these Official Rules. No reviews will be carried out for error-generating code.           
- Entrant must have all rights necessary to post and submit the entry.
- Each entry will be considered a contribution to the Mozilla open source project. As such, it is subject to [Mozilla’s Terms of Use](https://www.mozilla.org/en-US/about/legal/terms/mozilla/), which are expressly incorporated herein by reference. In particular, by submitting an entry, you agree to license your Submission under the terms of the corresponding license of the particular open source project to which you are contributing, in this case, the Mozilla Public License 2.0. For more information on the specific license, please see the applicable source code or GitHub repository.
- Each Entrant must be the maker of the submitted notebook.
- By entering this Promotion, each Entrant (either as an individual or a Team) certifies and represents that they remain in compliance with the Firefox Add-on Distribution Agreement they entered into when submitting their add-on for listing on addons.mozilla.org.
- Each Entrant must perform their analysis and submit their notebook during the Promotion Period, defined below.
- Entries may not contain likenesses of any individuals who are under 18 years of age or who have not provided their authorization. By submitting likeness of any individual under the age of majority in their jurisdiction of residence, you represent that you have received permission from such minor’s parent or legal guardian to include such minor’s image.
- Entries may not contain material that is obscene, defamatory, libelous, threatening, pornographic, racially or ethnically offensive, or which encourages conduct that would be considered a criminal offense, give rise to civil liability, or violate any law. Entries must be appropriate for viewing by the general public; appropriateness will be determined by Sponsor.
 
Sponsor reserves the right to reject any entry for any reason.
 
#### 3.    Promotion Period.  
This Promotion begins at 12:01 am PT on June 4, 2018 and ends at 11:59 pm PT on August 31, 2018 (the “Promotion Period”).  Sponsor’s computer is the official time-keeping device for the Promotion. All entries must be received during the dates and times specified in the Promotion Period.  
 
#### 4.    Eligibility.  
In order to be eligible, participants must: (i) be at least the age of majority in their jurisdiction of residence; and (ii) not be prohibited from participating by law, by company or employer policy, or by third-party agreement. In addition, employees of Sponsor and its parent and affiliate companies as well as the immediate family (spouse, parents, siblings and children) and household members of each such employee are not eligible. Entrants must be individuals or a team of no more than three individuals. Organizations such as corporations, educational institutions, non-profits or any other legal entities are not permitted to enter this Promotion.  
 
#### 5.    Winner(s). 
There will be one prize given to the winner of each of three Categories (defined and identified below). Winners will be announced by on or about September 14, 2018. The Categories are as follows:
 
- Tracking and Privacy
- Web Technologies and the Share of the Modern Web
- Equality, Neutrality, and Law
 
#### 6.     Judging.
Judging will be done by at least three employees of Sponsor and Sponsor shall have sole discretion in determining winners based on the following four, equally weighted criteria. The criteria are common to all Categories:
 
A. Scientific Approach – Sponsor will evaluate submissions based on adherence to scientific method. Intermediate assumptions should be validated and supporting evidence referenced to where results are interpreted.
 
B. Relevance to the 10 founding principles in Mozilla’s [Manifesto:](https://www.mozilla.org/en-US/about/manifesto/)
 
The internet is an integral part of modern life—a key component in education, communication, collaboration, business, entertainment and society as a whole.
The internet is a global public resource that must remain open and accessible.
The internet must enrich the lives of individual human beings.
Individuals’ security and privacy on the internet are fundamental and must not be treated as optional.
Individuals must have the ability to shape the internet and their own experiences on it.
The effectiveness of the internet as a public resource depends upon interoperability (protocols, data formats, content), innovation and decentralized participation worldwide.
Free and open source software promotes the development of the internet as a public resource.
Transparent community-based processes promote participation, accountability and trust.
Commercial involvement in the development of the internet brings many benefits; a balance between commercial profit and public benefit is critical.
Magnifying the public benefit aspects of the internet is an important goal, worthy of time, attention and commitment.
 
C. Relevance to one of the three Categories

Tracking and Privacy

Web Technologies and the Shape of the Modern Web

Equality, Neutrality, and Law
 
D. Creativity – Sponsor will evaluate submissions based on their innovative approach to data analysis and discovery of patterns in the data set that are not superficially obvious.
 
#### 7.    Prizes.
 
The winner in each Category will receive an invitation to attend MozFest. Sponsor will pay for the following for each winner, up to a total of $3,000.
Ticket to MozFest,
Airfare to and from MozFest,
Hotel accommodations during MozFest,
Any necessary visa fees.
 
At Sponsor’s discretion, each winner may be invited to present their findings in a 15-minute talk at MozFest.
 
Entrants should understand that attendance at MozFest and any time allotted are expressly conditioned on Entrant’s adherence the [Community Participation Guidelines.](https://www.mozilla.org/en-US/about/governance/policies/participation/)
 
The aggregate retail value of all the prize(s) is approximately $3,000.  Sponsor shall have final and sole discretion as to the particulars of the airfare hotel and visa fees for all prizes. No substitution, assignment or transfer of the prize is permitted, except by Sponsor, who has the right to substitute a prize with another of comparable or greater value. Winner is responsible for all taxes and fees associated with the receipt and/or use of the prize, and winner may be required to provide tax information prior to receiving the prize. Sponsor reserves the right to award prize to a Team’s agent, and it will be Team agent’s responsibility to divide the prize among Team members. Each Team member agrees to self-report to applicable taxing authorities, as may be required by applicable laws. Prize monies should be retained by individuals only in conformity with any applicable policies of his or her employers, academic institutions, or government regarding participation in and receipt of Promotional consideration relating to the Promotion and receipt and retention of prize. If a government, employer’s or school’s policies are applicable, it is the Entrant’s sole and ultimate responsibility, in consultation with his or her government, employer or school, to determine how and if prize will be retained and/or distributed and accounted for and we assume no responsibility for the decisions made by such government, employers or schools regarding this issue.

Each Team is solely responsible for its own cooperation and teamwork. In no event will Sponsor officiate in any dispute between or among any Team(s) or its/their members regarding their conduct, participation, cooperation or contribution. In the event that any dispute cannot be resolved, Sponsor reserves the right in its sole discretion to make a determination as to the identity of Team members or the team agent, and it may disqualify Teams and/or Team members in its sole discretion.

#### 8.    Conditions of Participation.  
By submitting an entry for this Promotion, you agree to abide by these rules and any decision Sponsor makes regarding this Promotion, which Sponsor shall make in its sole discretion.  Sponsor reserves the right to disqualify and prosecute to the fullest extent permitted by law any participant or winner who, in Sponsor’s reasonable suspicion, tampers with Sponsor site, the entry process, intentionally submits more than the allowed entries, violates these rules, or acts in an unsportsmanlike or disruptive manner.
 
#### 9.    Intellectual Property.  
By submitting an entry for this Promotion, you agree that your entry will be governed by the license available in the Github repository for this contest, specifically: [The Mozilla Public License.](https://www.mozilla.org/en-US/MPL/) Each participating Entrant hereby warrants that any entry and other materials and information provided by Entrant do not violate or infringe upon the copyrights, trademarks, rights of privacy, publicity, moral rights or other intellectual property or other rights of any person or entity, and do not violate any rules or regulations. If the entry or information or materials provided by Entrant contain any material or elements that are not owned by Entrant and/or which are subject to the rights of third parties, Entrant represents he or she has obtained, prior to submission of the entry and information or materials, any and all releases and consents necessary to permit use and exploitation of the entry and information and materials by Sponsor in the manner set forth in the Official Rules without additional compensation.  
 
Each Entrant warrants that the entry and materials and information provided do not contain information considered by Entrant, its employees or personnel, or any other third party to be confidential. Entrant agrees that Sponsor has the right to verify the ownership and originality of all entries and that, upon Sponsor’s request, Entrant must submit a written copy of any release or permission Entrant has received from a third party granting Entrant the right to use such property. Entrant understands and acknowledges that in the event a submission is selected as a winning entry, and Entrant’s ownership, rights and the originality of the entry cannot be verified to the satisfaction of Sponsor or is in any other way ineligible, Sponsor may select an alternate winner based on the same judging criteria. You acknowledge that other Entrants may submit entries that are similar to yours and that they, or Sponsor, may already be considering or developing, or may subsequently consider or develop independent of the Promotion, content or ideas that are related or similar to yours.  You acknowledge that this does not create in Sponsor or others any obligation or liability to you.
 
#### 10.    Disclaimer, Release and Limit of Liability.  
SPONSOR MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND, EXPRESS OR IMPLIED, REGARDING ANY PRIZE OR YOUR PARTICIPATION IN THE Promotion.  BY ENTERING THE Promotion OR RECEIPT OF ANY PRIZE, EACH Entrant  AGREES TO RELEASE AND HOLD HARMLESS SPONSOR AND ITS SUBSIDIARIES, AFFILIATES, SUPPLIERS, DISTRIBUTORS, ADVERTISING/Promotion AGENCIES, AND PRIZE SUPPLIERS, AND EACH OF THEIR RESPECTIVE PARENT COMPANIES AND EACH SUCH COMPANY’S OFFICERS, DIRECTORS, EMPLOYEES AND AGENTS (COLLECTIVELY, THE “RELEASED PARTIES”) FROM AND AGAINST ANY CLAIM OR CAUSE OF ACTION, INCLUDING, BUT NOT LIMITED TO, PERSONAL INJURY, DEATH, OR DAMAGE TO OR LOSS OF PROPERTY, ARISING OUT OF PARTICIPATION IN THE Promotion OR RECEIPT OR USE OR MISUSE OF ANY PRIZE.  THE RELEASED PARTIES ARE NOT RESPONSIBLE FOR:  (1) ANY INCORRECT OR INACCURATE INFORMATION, WHETHER CAUSED BY EntrantS, PRINTING ERRORS OR BY ANY OF THE EQUIPMENT OR PROGRAMMING ASSOCIATED WITH OR UTILIZED IN THE Promotion; (2) TECHNICAL FAILURES OF ANY KIND, INCLUDING, BUT NOT LIMITED TO MALFUNCTIONS, INTERRUPTIONS, OR DISCONNECTIONS IN PHONE LINES OR NETWORK HARDWARE OR SOFTWARE; (3) UNAUTHORIZED HUMAN INTERVENTION IN ANY PART OF THE ENTRY PROCESS OR THE Promotion; (4) TECHNICAL OR HUMAN ERROR WHICH MAY OCCUR IN THE ADMINISTRATION OF THE Promotion OR THE PROCESSING OF ENTRIES; OR (5) ANY INJURY OR DAMAGE TO PERSONS OR PROPERTY WHICH MAY BE CAUSED, DIRECTLY OR INDIRECTLY, IN WHOLE OR IN PART, FROM Entrant’S PARTICIPATION IN THE Promotion OR RECEIPT OR USE OR MISUSE OF ANY PRIZE.  

If for any reason an Entrant's entry is confirmed to have been erroneously deleted, lost, or otherwise destroyed or corrupted, Entrant’s sole remedy is another entry in the Promotion, provided that if it is not possible to award another entry due to discontinuance of the Promotion, or any part of it, for any reason, Sponsor, at its discretion, may elect to hold a random drawing from among all eligible entries received up to the date of discontinuance for any or all of the prizes offered herein.  No more than the stated number of prizes will be awarded. In event that production, technical, programming or any other reasons cause more than stated number of prizes as set forth in these Official Rules to be available and/or claimed Sponsor reserves the right to award only the stated number of prizes by a random drawing among all legitimate, unawarded, eligible prize claims.

#### 11.    Privacy and Use of Personal Information.  
Sponsor collects personal information from you when you enter this Promotion.  Sponsor reserves the right to use any information collected in accordance with its privacy policy, which may be found at https://www.mozilla.org/en-US/privacy/.
 
#### 12.    GOVERNING LAW AND DISPUTES. 
THESE OFFICIAL RULES AND THE Promotion ARE GOVERNED BY, AND WILL BE CONSTRUED IN ACCORDANCE WITH, THE LAWS OF THE STATE OF CALIFORNIA, AND THE FORUM AND VENUE FOR ANY DISPUTE ARISING OUT OF OR RELATING TO THESE OFFICIAL RULES SHALL BE IN SANTA CLARA COUNTY, CALIFORNIA. IF THE CONTROVERSY OR CLAIM IS NOT OTHERWISE RESOLVED THROUGH DIRECT DISCUSSIONS OR MEDIATION, IT SHALL THEN BE RESOLVED BY FINAL AND BINDING ARBITRATION ADMINISTERED BY JUDICIAL ARBITRATION AND MEDIATION SERVICES, INC., IN ACCORDANCE WITH ITS STREAMLINED ARBITRATION RULES AND PROCEDURES OR SUBSEQUENT VERSIONS THEREOF (“JAMS RULES”). THE JAMS RULES FOR SELECTION OF AN ARBITRATOR SHALL BE FOLLOWED, EXCEPT THAT THE ARBITRATOR SHALL BE EXPERIENCED AND LICENSED TO PRACTICE LAW IN CALIFORNIA. ANY SUCH CONTROVERSY OR CLAIM WILL BE ARBITRATED ON AN INDIVIDUAL BASIS, AND WILL NOT BE CONSOLIDATED IN ANY ARBITRATION WITH ANY CLAIM OR CONTROVERSY OF ANY OTHER PARTY. ALL PROCEEDINGS BROUGHT PURSUANT TO THIS PARAGRAPH WILL BE CONDUCTED IN SANTA CLARA COUNTY, CALIFORNIA. THE REMEDY FOR ANY CLAIM SHALL BE LIMITED TO ACTUAL DAMAGES, AND IN NO EVENT SHALL ANY PARTY BE ENTITLED TO RECOVER PUNITIVE, EXEMPLARY, CONSEQUENTIAL, OR INCIDENTAL DAMAGES, INCLUDING ATTORNEY’S FEES OR OTHER SUCH RELATED COSTS OF BRINGING A CLAIM, OR TO RESCIND THIS AGREEMENT OR SEEK INJUNCTIVE OR ANY OTHER EQUITABLE RELIEF.
 
#### 13.    Publicity Grant.  
Except where prohibited, participation in the Promotion constitutes Entrant’s consent to Sponsor’s and Sponsor’s designees’ publication, broadcast, display, sharing and use of Entrant’s name, likeness, voice, image, persona, biographical information, entry and audio and visual content shared by Entrant for any purposes in any media, worldwide, without further payment or consideration.
 
#### 14.    Confidentiality.  
Submissions will be shared with others and portions of entries may be reproduced elsewhere, including in connection with Promotion-related publicity materials.  You should not disclose any information in your entry that is proprietary or confidential.  No confidential relationship is established between you and Sponsor in connection with your entry.

#### 15.    Winners List.  
Individuals may request the name of winner(s) by submitting a self-addressed stamped envelope prior to October 1, 2018 to Overscripted Web: A Mozilla Data Analysis Challenge Winner’s List Request, 331 E. Evelyn Ave., Mountain View, CA 94041.  Vermont residents may omit postage.
 




