OJT Project Design Template

**Student** **Name(s):** Parth Mozarkar & Anirudh Gupta **Roll**
**No(s):** 251810700101, 251810700194

**Year** **&** **Section:** Semester 1(A)

**Project** **Title** **(as** **assigned):** Quiz Engine CLI with Item
Bank & Scoring **Project** **Type:** Product Developing

**Stack** **/** **Framework:** Python CLI, JSON, CSV

> 1\. Problem Understanding

**1.1** **What** **is** **the** **problem** **statement** **in**
**your** **own** **words?**

*Many* *students* *struggle* *to* *practice* *quizzes* *or* *test*
*their* *knowledge* *without* *relying* *on* *online* *tools.* *Most*
*quiz* *applications* *today* *are* *web-based* *or* *require* *a*
*complex* *setup.* *This* *project* *solves* *that* *problem* *by*
*developing* *a* *Python-based* *command-line* *quiz* *engine* *that*
*runs* *offline,* *uses* *a* *question* *bank* *from* *a* *JSON* *or*
*CSV,* *and* *automatically* *evaluates* *and* *scores* *users.*

**1.2** **Why** **does** **this** **problem** **exist** **or**
**matter?**

*This* *problem* *exists* *because* *most* *quiz* *or* *test* *systems*
*today* *depend* *on* *web* *technologies* *and* *constant* *internet*
*access.* *However,* *in* *many* *educational* *and* *training*
*environments,* *especially* *during* *offline* *sessions* *or*
*limited* *network* *areas,* *learners* *and* *teachers* *need* *a*
*lightweight,* *fast,* *and* *offline* *alternative.* *A* *Quiz*
*Engine* *CLI* *matters* *because:* *It* *allows* *offline* *quizzes*
*anytime,* *anywhere.* *It* *is* *also* *simple* *and* *efficient.* *It*
*also* *supports* *custom* *question* *banks* *and* *helps* *developers*
*practice* *real-world* *logic.*

**1.3** **Key** **inputs** **and** **expected** **outputs:**

||
||
||
||
||
||
||

> 2\. Functional Scope

**2.1** **What** **are** **the** **core** **features** **you** **plan**
**to** **build** **(must-haves)?** *1.* *Load* *quiz* *questions* *from*
*a* *JSON/CSV* *item* *bank.*

*2.* *Display* *multiple-choice* *questions* *in* *CLI.*

*3.* *Accept* *user* *input* *and* *evaluate* *answers.*

*4.* *Auto-calculate* *total* *score* *and* *percentage.*

*5.* *Save* *score* *and* *user* *info* *into* *a* *CSV* *file*

**2.2** **What** **stretch** **goals** **could** **you** **attempt**
**if** **time** **permits?** *•* *Add* *difficulty* *levels* *(Easy,*
*Medium,* *Hard).*

*•* *Implement* *a* *timer* *for* *each* *question.*

*•* *Allow* *admin* *mode* *to* *add/edit* *questions.*

*•* *Display* *quiz* *summary* *with* *percentages* *and* *grades*

**2.3** **Which** **libraries** **or** **tools** **will** **you**
**use?** *•* *Python* *3.x* *(core* *language)*

*•* *JSON* *for* *question* *storage* *•*

*CSV* *for* *score* *tracking*

*•* *Random* *module* *for* *question* *shuffling*

*•* *Datetime* *for* *saving* *timestamps*

> 3.System & Design Thinking

**3.1** **Sketch** **or** **describe** **your** **app** **flow** **/**
**pipeline:** **~** *Start* *Program*

> *→* *Get* *User* *Name*

*→* *Load* *Questions* *from* *Item* *Bank*

*→* *Randomize* *Order*

> *→* *Display* *Each* *Question*
>
> *→* *Get* *User* *Answer*

*→* *Check* *Correctness*

> *→* *Calculate* *Total* *Score*
>
> *→* *Display* *Results*
>
> *→* *Save* *Score* *to* *File*

*→* *End*

**3.2** **What** **data** **structures** **or** **algorithms** **are**
**central** **to** **this** **project?** *•* *Lists* *and*
*Dictionaries* *for* *question* *handling.*

*•* *File* *handling* *(JSON* *&* *CSV)* *for* *input/output.*

> *•* *Randomization* *algorithm* *for* *selecting* *question* *order.*

*•* *Datetime* *for* *recording* *timestamps*

**3.3** **How** **will** **you** **test** **correctness** **or**
**performance?** *•* *Manual* *testing* *with* *different* *datasets.*

*•* *Validation* *of* *input* *(wrong* *keys,* *empty* *answers).*

*•* *Output* *verification* *for* *correct* *scoring.*

> 4.Timeline & Milestones (4 Weeks)

||
||
||
||

||
||
||
||
||

> 5.Risks & Dependencies

**5.1** **What’s** **the** **hardest** **part** **technically** **for**
**you** **right** **now?** *•* *Managing* *file* *read/write*
*operations* *efficiently.*

*•* *Handling* *invalid* *user* *inputs* *and* *maintaining* *smooth*
*CLI* *flow.*

*•* *Designing* *reusable* *functions* *for* *logic* *and* *scoring.*

**5.2** **What** **dependencies** **or** **help** **do** **you**
**need** **from** **mentors?** *•* *Guidance* *for* *optimizing*
*Python* *structure.*

*•* *Review* *scoring* *logic* *and* *leaderboard* *design.*

*•* *Validation* *of* *question* *bank* *format.*

> 6.Evaluation Readiness

**6.1** **How** **will** **you** **prove** **that** **your** **project**
**“works”?** *•* *Demo* *video* *of* *quiz* *running* *in* *command*
*prompt.*

*•* *Screenshots* *of* *input,* *output,* *and* *leaderboard.*

*•* *GitHub* *repository* *link* *with* *source* *code.*

*•* *PRD* *and* *documentation* *file.*

**6.2** **What** **success** **metric** **or** **goal** **will** **you**
**aim** **for?** *•* *100%* *correct* *input/output* *flow.*

> *•* *Zero* *runtime* *errors.*
>
> *•* *All* *quiz* *attempts* *recorded* *in* *CSV.*

*•* *Functional* *leaderboard* *and* *result* *display*

> 7.Responsibilities

**7.1** **Responsibilities**

||
||
||
||
||
||
||
||

> 8.Student Accessible Features
>
> • Take quiz from CLI (multiple attempts allowed).
>
> • View immediate score and correctness per question. • View percentage
> and cumulative performance.
>
> • Retry quizzes and select subsets if implemented. • View leaderboard
> (local CSV-based).
>
> 9.Admin Accessible Features
>
> • Add / edit / delete questions via admin mode.
>
> • Upload JSON/CSV question banks following template. • View all user
> scores and export leaderboard.
>
> • Reset or clear leaderboard.
>
> • Configure quiz settings (shuffle, time limits, difficulty).
>
> 10\. User Limitations & Constraints
>
> • Runs only in local machine terminal (no GUI).
>
> • Offline-only: features requiring internet are not supported. •
> Supports MCQ format only (no long answer questions).
>
> • Input files must conform to provided JSON/CSV schema. • Large
> question banks may increase memory and runtime.
>
> • No concurrent multi-user operation; single-user CLI sessions only.
>
> 11\. User Details & Context of Use
>
> **Primary** **Users:**
>
> • Students preparing for exams in offline environments. • Teachers
> needing quick, offline assessment tools. **Needs:**
>
> • Fast, lightweight quiz execution without internet. • Instant scoring
> and local result storage.
>
> **Context** **of** **Use:**
>
> • College labs, offline classrooms, low-resource systems, self-study.
>
> 12\. Project Folder Structure
>
> project_root/ main.py quiz_engine/ \_\_init\_\_.py
> [<u>loader.py</u>](http://loader.py/) evaluator.py scorer.py
> [<u>admin.py</u>](http://admin.py) data/
>
> Questions.json Leaderboard.csv docs/
>
> PRD.pdf tests/
>
> Test_loader.py Test_scorer.py README.md
>
> 13\. Testing Strategies (Detailed)
>
> **Functional** **Testing:** - Verify question loading, display
> ordering, answer acceptance, scoring, and result saving. Input
>
> **Validation** **Testing:** - Provide malformed JSON/CSV, invalid
> option keys, and empty answers to ensure graceful handling and error
> me
>
> **Boundary** **Testing:** - Test with very large question banks, and
> with zero questions to check limits and behavior.
>
> **Scenario-Based** **Testing:** - Simulate full user flows, corrupt
> files, and interrupted runs to validate robustness.
>
> **Automated** **Unit** **Tests:** - Create unit tests for loader.py,
> evaluator.py, and scorer.py; run via pytest and place under /tests.
>
> **Integration** **Testing:** - End-to-end tests that run the CLI,
> perform a quiz, and confirm leaderboard persistence.
>
> **Performance** **Testing:** - Measure load time and memory usage with
> increasing question bank sizes.
>
> **User** **Acceptance** **Testing** **(UAT):** - Have sample
> students/mentors run the quiz and confirm behavior matches
> expectations.

**Signatures** **(Students):** **Parth** **Mozarkar** **&** **Anirudh**
**Gupta**

**Mentor** **Approval:**

**Date:** 18/11/2025
