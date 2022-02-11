# GUIDANCE

The function of our website can be divided into three components. 

The first function is predicting the secondary structure of specified RNA sequence, you just need to input a FASTA formated RNA sequence(composed of ATCGU or atcgu) and then click the button located below the input box. The software will return a web interface for displaying RNA secondary structures, you can even drag the specified bases you want to observe their structural changes. The website also provides an example for display. Tap `EXAMPLE` and click the button below, and you will see the most accurate prediction of RNA secondary structure. If the sequence you entered contains bases other than ATCGU (atcgu), you will receive an error message.

Apart from that, The second function of the website is to evaluate whether the probe designed by the user will hybridize with other nucleic acid substance sequences in a specific biological environment, and to assign a score based on this. The user first enters the target sequence (most are the probes you've designed), and then enters the sequence of other nucleic acid substances in the environment, each sequence is separated by a `SPACE`. Don’t forget to enter the total number of sequences in the input box above (the number of target sequences + the number of other sequences).Remember that the sequences entered should also be composed of ATCGU(atcgu).  We will soon return a score, and you can use the score to judge whether the probe you designed can function well in the specific biological environment without being too disturbed by the other sequences. A score less than 50 indicates that the probe is working well. The higher the score is, the more the probe is disturbed by the environment and the more serious the hybridization is. You can also click on `EXAMPLE` to view the demonstration. If the number you entered is inconsistent with the number of sequences you entered, you will also receive an error message.



