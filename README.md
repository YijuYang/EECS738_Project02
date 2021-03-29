# Project 2 - Hidden Mark.. M..


## Probabilistic states and transitions
1. Set up a new git repository in your GitHub account
2. Pick a text corpus dataset such as https://www.kaggle.com/kingburrito666/shakespeare-plays or from https://github.com/niderhoff/nlp-datasets
3. Choose a programming language (Python, C/C++, Java)
4. Formulate ideas on how machine learning can be used to learn word correlations and distributions within the dataset
5. Build a Hidden Markov Model to be able to programmatically
   1. Generate new text from the text corpus
   2. Perform text prediction given a sequence of words
6. Document your process and results
7. Commit your source code, documentation and other supporting files to the git repository in GitHub


## Dataset
#### Context
This is all of Shakespeare's plays.

#### Content
This is a dataset comprised of all of Shakespeare's plays. It includes the following:

The first column is the Data-Line, it just keeps track of all the
rows there are.
The second column is the play that the lines are from.
The third column is the actual line being spoken at any given time.
The fourth column is the Act-Scene-Line from which any given line is
from.
The fifth column is the player who is saying any given line.
The sixth column is the line being spoken.
#### Inspiration
I've been doing Shakespeare for a while and I wanted to make a Shakespearean chatbot.


## Settings
The program starts the text generation process with a fixed number of lines (30). The first, second and third words of each line are selected from the "firstWords", "secondWords" and "thirdWords" dictionaries respectively. Randomly select the first word among the first words that appear in the training set. Choose the second word based on the first word. Choose the third word based on the first two words.
Starting from the fourth word in each line, a Markov chain is used to predict the word. Initially, we tried to use the thirdOrder dictionary to predict the next word in a row based on the first three words.
Each line ends when either we have reached a dead end in all three Markov chains or we have reached the words per line limit (15).

## Output example
1 :  lofty and stops my breath and little is to fear and sleep that i got this
2 :  boldness of valiant shirley stafford are strewings fittst for itself itself into happiness upon was touchd
3 :  thrive long continuance in illyria whatsoever they nothing doubt you not for praising caesar they raind
4 :  cause they do bend my speech should tread and hortensius and timon of disdain but for
5 :  blaspheming god ild you for good will and your maids could out dunghill darest bring oil
6 :  mines the bow is curst have informd for charity itself each on one leg the tongue
7 :  watch thou troublest me dangerous is landed is tame a shrew you clappd to blazon it
8 :  constantinople and back again this is hers is set our men rebellion against your highness claim
9 :  calpurnia here art that likewise your fashion madam not yet at last to comfort them accomplished
10 :  palaces treason is but faintly nothing like the noble duke at morning may equally a gain
11 :  entreaty and speakt again again not sort to warwick my lord sands you heap must endure
12 :  coy looks it dear juliet wakes why helen attended at slackness canidius we be merry yet
13 :  unfurnish me shall gain nothing but mortimer which draught in silence sad stop me your petition
14 :  salvation body as a lords again lay our best mercy for everlasting bond which wood woman
15 :  different namessure moreand these young ones teach the dam will overhear their wills their force gainst
16 :  grecian thou desirest me mighty kings this man did calculate my humanity come thou boyqueller show
17 :  thats but macbeth and an injury i your wish my will as item it rages and
18 :  piercing a matter abhor it flame to saintseducing gold without true descent than fear makes amends
19 :  crave your horse as tibs
20 :  prepared i mock my destruction than on her look her circled orb which bears fire thats
21 :  misthink the undoing all a more riotous madness wherein olivia with malvolio is place reserved you
22 :  board em i think might never stir from meaner than did laugh sans eyes no disjunction
23 :  hoist with ribands pendent rock yet taste confounds me present power ont but i must make
24 :  coach good a lady that disdains to datchetmead and while i pause serve love sincere verity
25 :  blasting his absolute commission i believe there let it keep o send ministers and come ye
26 :  petticoat and kept asunder you directly in antonius beard made himself theres not a one that
27 :  accountyet who having been three pound lift them gentle lover but gracious henry but seven or
28 :  war death having vowd revenge farewell ill adventure hath hither armd rhinoceros or scold your bounties
29 :  produce the prisoner fare the gracious utterance of my great affliction off guilty my nativity chance
30 :  danger and soundly with eye see see my mothers breath left mine ancestor thy imperial mistress
