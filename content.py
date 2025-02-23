from IPython.display import display, HTML
import numpy as np



# Add LaTeX-style CSS
css_content = HTML("""
<style>
:root {
    /* Size variables */
    --slide-max-width: 1900px;
    --base-font-size: 20px;
    --spacing-unit: 15px;
    
    /* Font size scale */
    --h1-size: 2.5em;    /* section */
    --h2-size: 2.2em;    /* subsection */
    --h3-size: 1.8em;    /* section-title */
    --h4-size: 1.2em;    /* example-title */
    --small-text: 0.9em;
    
    /* Colors */
    --primary-color: #2980b9;
    --secondary-color: #3498db;
    --text-color: #333;
    --light-bg: #f8f9fa;
    --error-color: #e53935;
    --success-color: #c8e6c9;
    
    /* Shadows */
    --box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.latex-container {
    max-width: var(--slide-max-width);
    margin: calc(var(--spacing-unit) + 5px) auto;
    font-family: 'Computer Modern', serif;
    line-height: 1.6;
    color: var(--text-color);
    font-size: var(--base-font-size);
}

.section-title {
    font-size: var(--h3-size);
    color: #2c3e50;
    margin: var(--spacing-unit) 0;
    font-weight: bold;
    border-bottom: 2px solid var(--secondary-color);
    padding-bottom: calc(var(--spacing-unit) - 5px);
    text-align: center;
}

.chapter {
    font-size: var(--h1-size);
    color: #2c3e50;
    margin: var(--spacing-unit) 0;
    font-weight: bold;
}

.section {
    font-size: var(--h1-size);
    color: #34495e;
    margin: calc(var(--spacing-unit) + 10px) 0;
}

.subsection {
    font-size: var(--h2-size);
    color: var(--primary-color);
    margin: var(--spacing-unit) 0;
}

.content-box, .definition-box {
    background-color: var(--light-bg);
    border-left: 4px solid var(--primary-color);
    padding: var(--spacing-unit);
    margin: var(--spacing-unit) 0;
    box-shadow: var(--box-shadow);
}

.definition {
    background-color: #e8f4f8;
    border-radius: 4px;
    padding: var(--spacing-unit);
    margin: var(--spacing-unit) 0;
}

.example-box {
    background-color: var(--light-bg);
    border: 1px solid #dee2e6;
    border-radius: 4px;
    padding: var(--spacing-unit);
    margin: var(--spacing-unit) 0;
    box-shadow: var(--box-shadow);
}

.example-title {
    font-size: var(--h4-size);
    color: #2c3e50;
    margin-bottom: var(--spacing-unit);
    font-weight: bold;
}

.communication-diagram {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 30px 0;
    padding: 20px;
    background: #fff;
    border-radius: 8px;
}

.sender, .receiver {
    background: #e3f2fd;
    padding: 15px;
    border-radius: 8px;
    width: 150px;
    text-align: center;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.channel {
    flex-grow: 1;
    margin: 0 20px;
    position: relative;
    height: 4px;
    background: #90caf9;
}

.error {
    position: absolute;
    top: calc(-1 * var(--spacing-unit));
    color: var(--error-color);
    font-size: var(--small-text);
}

.message {
    background: var(--success-color);
    padding: calc(var(--spacing-unit) - 7px);
    margin: calc(var(--spacing-unit) - 5px) 0;
    border-radius: 4px;
}

.error-message {
    background: #ffcdd2;
}

.note {
    font-style: italic;
    color: #666;
    margin-top: var(--spacing-unit);
    font-size: var(--small-text);
}

.key-term {
    color: #2980b9;
    font-weight: bold;
}

.math {
    font-style: italic;
}

.encoding-table {
    margin: 20px auto;
    border-collapse: collapse;
}

.encoding-table td {
    padding: 8px 15px;
    text-align: center;
}

.arrow {
    color: #666;
    padding: 0 10px;
}

.equation {
    text-align: center;
    margin: 20px 0;
    font-style: italic;
    font-size: 1.1em;
    color: #2c3e50;
}

.hamming-table {
    border-collapse: collapse;
    margin: 20px auto;
    font-size: 14px;
    background: white;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.hamming-table th, .hamming-table td {
    border: 1px solid #ddd;
    padding: 12px;
    text-align: center;
    transition: background-color 0.2s;
}

.hamming-table th {
    background-color: #f8f9fa;
    font-weight: normal;
    color: #333;
}

.hamming-table tr:hover {
    background-color: #f5f5f5;
}

.table-title {
    text-align: center;
    font-size: 16px;
    margin-bottom: 15px;
    font-style: italic;
    color: #333;
}

.min-distance {
    text-align: center;
    margin-top: 15px;
    font-style: italic;
    color: #333;
}

.theorem, .proposition, .proof, .example {
    background-color: #f8f9fa;
    border-left: 4px solid #2980b9;
    padding: 20px;
    margin: 15px 0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.important-note {
    background-color: #fff3e0;
    border-left: 4px solid #ff9800;
    padding: 15px;
    margin: 15px 0;
}

.matrix-display {
    background-color: #fff;
    padding: 15px;
    border-radius: 4px;
    margin: 10px 0;
    text-align: center;
    font-family: 'Computer Modern Math', serif;
}

.calculation {
    background-color: #e8f6f3;
    padding: 15px;
    border-radius: 4px;
    margin: 10px 0;
}
</style>
""")
display(css_content)

def create_intro_section():
    """
    basic content:

    # 1. Coding Theory Basics

    ## What is coding theory?

    1.1 The basic problem of coding theory is that of communication over an unreliable channel that results in errors
    in the transmitted message.

    The aim of coding is to modify data in a way, such that random errors, that occur
    during the transmission, can be detected or even corrected.
    """

    
    # Create the content
    html_content = """
    <div class="latex-container">
        <div class="chapter">1. Coding Theory Basics</div>
        
        <div class="section">What is coding theory?</div>
        
        <div class="content-box">
            <div class="subsection">1.1 The Basic Problem</div>
            
            <p>The basic problem of coding theory is that of communication over an unreliable channel 
            that results in errors in the transmitted message.</p>
            
            <div class="definition">
                <p>The aim of coding is to modify data in a way, such that random errors, that occur
                during the transmission, can be:</p>
                <ul>
                    <li>Detected</li>
                    <li>Corrected</li>
                </ul>
            </div>
        </div>
    </div>
    """
    
    display(HTML(html_content))



def create_communication_example():
    
    html_content = """
    <div class="latex-container">
        <div class="example-box">
            <div class="example-title">Example: Basic Communication Channel</div>
            
            <div class="communication-diagram">
                <div class="sender">
                    <strong>Sender</strong>
                    <div class="message">1011</div>
                </div>
                
                <div class="channel">
                    <div class="error">⚡ Noise/Error</div>
                </div>
                
                <div class="receiver">
                    <strong>Receiver</strong>
                    <div class="message error-message">1001</div>
                </div>
            </div>

            <div class="example-box">
                <strong>Common Scenarios:</strong>
                <ol>
                    <li>
                        <strong>Perfect Transmission:</strong><br>
                        Sent: 1011 → Received: 1011
                    </li>
                    <li>
                        <strong>Single-bit Error:</strong><br>
                        Sent: 1011 → Received: 1001 (3rd bit flipped)
                    </li>
                    <li>
                        <strong>Multiple-bit Error:</strong><br>
                        Sent: 1011 → Received: 0010 (several bits flipped)
                    </li>
                </ol>
            </div>

            <div class="note">
                <p><strong>Key Points:</strong></p>
                <ul>
                    <li>The channel can introduce errors due to noise, interference, or other factors</li>
                    <li>Without error detection/correction, the receiver cannot identify if the message was corrupted</li>
                    <li>Coding theory provides methods to detect and correct these transmission errors</li>
                </ul>
            </div>
        </div>
    </div>
    """
    
    display(HTML(html_content))


def create_coding_section():

    """
    basic content:
### Coding


For this purpose redundancy is added to the original data which makes the data more "distinguishable" from
each other. This makes it is easier to find out if errors have occurred or even which
errors these were and to restore the original data.

In our context data are words over a given alphabet. The modified data words
are called codewords and are words over the same alphabet. The set of all these
codewords is called code and the transition from the original word to the codeword
is called encoding. In this work we consider only so called block codes, where all
codewords have the same length.

    """
   
    
    html_content = """
    <div class="latex-container">
        <div class="section-title">Coding</div>
        
        <div class="content-box">
            <p>For this purpose <span class="key-term">redundancy</span> is added to the original data 
            which makes the data more "distinguishable" from each other. This makes it easier to:</p>
            <ul>
                <li>Detect if errors have occurred</li>
                <li>Identify which errors occurred</li>
                <li>Restore the original data</li>
            </ul>
        </div>

        <div class="definition">
            <p><strong>Key Concepts:</strong></p>
            <ul>
                <li><span class="key-term">Data Words:</span> Words over a given alphabet</li>
                <li><span class="key-term">Codewords:</span> Modified data words over the same alphabet</li>
                <li><span class="key-term">Code:</span> The set of all codewords</li>
                <li><span class="key-term">Encoding:</span> The transition from the original word to the codeword</li>
            </ul>
            
            <div class="note">
                <p><strong>Note:</strong> In this work, we consider only so-called <span class="key-term">block codes</span>, 
                where all codewords have the same length.</p>
            </div>
        </div>
    </div>
    """
    
    display(HTML(html_content))


def create_decoding_section():
    """
    basic content:
    
    ### Decoding

    Now suppose that a codeword c is sent over a channel and the word x is received.
    The receiver knows that a codeword was sent and when x is a codeword, he assumes
    that x is the correct codeword. Otherwise he knows that errors have occurred. De-
    pending on the application he than has the possibility to request the codeword cagain
    or has to deduce the sent codeword cfrom x. The process of assigning a codeword to
    a received word is called decoding.
    """
    
    html_content = """
    <div class="latex-container">
        <div class="section-title">Decoding</div>
        
        <div class="content-box">
            <p>Now suppose that a codeword <span class="math">c</span> is sent over a channel and 
            the word <span class="math">x</span> is received.</p>
            
            <div class="communication-diagram">
                <div class="sender">
                    <strong>Sender</strong>
                    <div class="message">c = 1100</div>
                </div>
                
                <div class="channel">
                    <div class="error">⚡ Error</div>
                </div>
                
                <div class="receiver">
                    <strong>Receiver</strong>
                    <div class="message error-message">x = 1110</div>
                </div>
            </div>

            <div class="definition">
                <p><strong>Decoding Process:</strong></p>
                <ul>
                    <li>When <span class="math">x</span> is a codeword, the receiver assumes it is the correct codeword</li>
                    <li>Otherwise, errors have occurred during transmission</li>
                </ul>
            </div>

            <div class="example-box">
                <p><strong>Error Handling Options:</strong></p>
                <ol>
                    <li>Request the codeword <span class="math">c</span> to be sent again</li>
                    <li>Attempt to deduce the sent codeword <span class="math">c</span> from the received word <span class="math">x</span></li>
                </ol>
            </div>

            <div class="definition-box">
                <p><strong>Definition:</strong> The process of assigning a codeword to a received word is called 
                <span class="key-term">decoding</span>.</p>
            </div>

            <div class="example-box">
                <div class="example-title">Decoding Process Flow</div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
                    <div style="text-align: center; padding: 10px; background: #e3f2fd; border-radius: 8px; width: 150px;">
                        <strong>Received Word</strong>
                        <div class="message">x = 1110</div>
                    </div>
                    <div style="text-align: center;">
                        <span style="font-size: 24px;">→</span>
                    </div>
                    <div style="text-align: center; padding: 10px; background: #e8f5e9; border-radius: 8px; width: 150px;">
                        <strong>Check if Codeword</strong>
                        <div>Not in Code</div>
                    </div>
                    <div style="text-align: center;">
                        <span style="font-size: 24px;">→</span>
                    </div>
                    <div style="text-align: center; padding: 10px; background: #fff3e0; border-radius: 8px; width: 150px;">
                        <strong>Decode</strong>
                        <div class="message">c = 1100</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
    
    display(HTML(html_content))


def create_coding_example():
    """
    basic content:
    ### Example

    Consider the alphabet A= Z_2 and the binary block code
    C= {(0,0,0,0),(0,0,1,1),(0,1,0,1),(0,1,1,0),
    (1,0,0,1),(1,0,1,0),(1,1,0,0),(1,1,1,1)}⊆A^4

    The codewords come from the eight data words (0,0,0), (0,0,1), (0,1,0), (0,1,1),(1,0,0), (1,0,1), (1,1,0), (1,1,1) ∈ A^3 which are encoded by adding the following redundancy bits


    (0,0,0) →(0,0,0,0) (1,0,0) →(1,0,0,1)
    (0,0,1) →(0,0,1,1) (1,0,1) →(1,0,1,0)
    (0,1,0) →(0,1,0,1) (1,1,0) →(1,1,0,0)
    (0,1,1) →(0,1,1,0) (1,1,1) →(1,1,1,1).


    Cis a so-called parity check code where the original words are encoded by adding a
    parity check bit, such that each codeword has an even number of ones.

    """
  
    
    html_content = """
    <div class="latex-container">
        <div class="example-box">
            <div class="example-title">Example: Binary Block Code</div>
            
            <p>Consider the alphabet <span class="math">A = Z₂</span> and the binary block code:</p>
            <p class="math">
                C = {(0,0,0,0), (0,0,1,1), (0,1,0,1), (0,1,1,0),<br>
                     (1,0,0,1), (1,0,1,0), (1,1,0,0), (1,1,1,1)} ⊆ A⁴
            </p>
            
            <p>The codewords come from the eight data words in <span class="math">A³</span>, 
            encoded with redundancy bits as follows:</p>
            
            <table class="encoding-table">
                <tr>
                    <td>(0,0,0)</td><td class="arrow">→</td><td>(0,0,0,0)</td>
                    <td width="20"></td>
                    <td>(1,0,0)</td><td class="arrow">→</td><td>(1,0,0,1)</td>
                </tr>
                <tr>
                    <td>(0,0,1)</td><td class="arrow">→</td><td>(0,0,1,1)</td>
                    <td width="20"></td>
                    <td>(1,0,1)</td><td class="arrow">→</td><td>(1,0,1,0)</td>
                </tr>
                <tr>
                    <td>(0,1,0)</td><td class="arrow">→</td><td>(0,1,0,1)</td>
                    <td width="20"></td>
                    <td>(1,1,0)</td><td class="arrow">→</td><td>(1,1,0,0)</td>
                </tr>
                <tr>
                    <td>(0,1,1)</td><td class="arrow">→</td><td>(0,1,1,0)</td>
                    <td width="20"></td>
                    <td>(1,1,1)</td><td class="arrow">→</td><td>(1,1,1,1)</td>
                </tr>
            </table>
            
            <div class="definition">
                <p>This is a parity check code where the original words are encoded by adding a
                parity check bit, such that each codeword has an even number of ones.</p>
            </div>

            <div class="example-box">
                <div class="example-title">Decoding Example</div>
                
                <div class="communication-diagram">
                    <div class="sender">
                        <strong>Original Codeword</strong>
                        <div class="message">c = (1,1,0,0)</div>
                        <div class="note">Even parity ✓</div>
                    </div>
                    
                    <div class="channel">
                        <div class="error">⚡ Bit Flip</div>
                    </div>
                    
                    <div class="receiver">
                        <strong>Received Word</strong>
                        <div class="message error-message">x = (1,1,0,1)</div>
                        <div class="note">Odd parity ✗</div>
                    </div>
                </div>

                <div style="display: flex; justify-content: center; align-items: center; margin: 20px 0;">
                    <div style="text-align: center;">
                        <strong>Decoding Steps</strong>
                        <div style="display: flex; align-items: center; margin-top: 10px;">
                            <div style="background: #e3f2fd; padding: 10px; border-radius: 8px;">
                                <div>Received</div>
                                <div class="message">(1,1,0,1)</div>
                            </div>
                            <div style="margin: 0 15px;">→</div>
                            <div style="background: #fff3e0; padding: 10px; border-radius: 8px;">
                                <div>Check Parity</div>
                                <div>Odd Count: 3</div>
                            </div>
                            <div style="margin: 0 15px;">→</div>
                            <div style="background: #e8f5e9; padding: 10px; border-radius: 8px;">
                                <div>Nearest Codeword</div>
                                <div class="message">(1,1,0,0)</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="example-box">
                <div class="example-title">Minimum Distance Analysis</div>
                
                <div style="display: flex; justify-content: space-around; align-items: center; margin: 20px 0;">
                    <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 8px;">
                        <strong>Example Pair</strong>
                        <div class="message">
                            c₁ = (0,0,0,0)<br>
                            c₂ = (0,0,1,1)
                        </div>
                        <div class="note">d(c₁,c₂) = 2</div>
                    </div>
                    
                    <div style="text-align: center; padding: 15px; background: #fff3e0; border-radius: 8px;">
                        <strong>Minimum Distance</strong>
                        <div class="message">d(C) = 2</div>
                        <div class="note">All pairs differ in<br>at least 2 positions</div>
                    </div>
                    
                    <div style="text-align: center; padding: 15px; background: #e8f5e9; border-radius: 8px;">
                        <strong>Capabilities</strong>
                        <ul style="text-align: left; margin: 5px 0;">
                            <li>Can detect 1 error</li>
                            <li>Cannot correct errors</li>
                        </ul>
                    </div>
                </div>

                <div class="note">
                    <p><strong>Why d(C) = 2?</strong></p>
                    <ul>
                        <li>Every codeword has even parity</li>
                        <li>Any single bit flip creates odd parity</li>
                        <li>Therefore, any two codewords must differ in at least 2 positions</li>
                        <li>Some pairs (like shown above) differ in exactly 2 positions</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    """
    
    display(HTML(html_content))


def create_minimum_distance_section():
    html_content = """
    <div class="latex-container">
            <div class="section-title">Minimum Distance</div>
            
        <div class="content-box">
            <div class="definition-box">
                <p><strong>Hamming Distance</strong></p>
                <p>For vectors x,y ∈ {0,1}ⁿ, the Hamming distance d(x,y) is the number of positions where they differ.</p>
                
                <div class="example-box">
                    <div class="example-title">Example</div>
                    <div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
                        <div>
                            x = <span class="math">(1,0,1,1)</span><br>
                            y = <span class="math">(1,1,1,0)</span>
                </div>
                        <div>→</div>
                        <div>
                            d(x,y) = 2<br>
                            <span class="note">(differs in positions 2 and 4)</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="definition-box">
                <p><strong>Minimum Distance of a Code</strong></p>
                <p>The minimum distance d(C) of a code C is the smallest Hamming distance between any two different codewords.</p>
                
                <div class="example-box">
                    <div style="display: flex; justify-content: center; align-items: center; margin: 10px 0;">
                        <div style="text-align: center; padding: 10px; background: #e3f2fd; border-radius: 8px;">
                            <strong>Code C</strong>
                            <div class="message">
                                (0,0,0)<br>
                                (1,1,0)<br>
                                (0,1,1)
                            </div>
                        </div>
                        <div style="margin: 0 15px;">→</div>
                        <div style="text-align: center; padding: 10px; background: #e8f5e9; border-radius: 8px;">
                            <strong>d(C) = 2</strong>
                            <div class="note">Minimum among all<br>pairwise distances</div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="note">
                <p><strong>Key Application:</strong> The minimum distance determines the code's error-detecting 
                and error-correcting capabilities.</p>
            </div>
        </div>
    </div>
    """
    
    display(HTML(html_content))





# Define the codewords
codewords = np.array([
    [0,0,0,0], [0,0,1,1], [0,1,0,1], [0,1,1,0],
    [1,0,0,1], [1,0,1,0], [1,1,0,0], [1,1,1,1]
])

def hamming_distance(x, y):
    """Calculate Hamming distance between two vectors"""
    return np.sum(x != y)

def create_distance_table():
    
    """
    basic content:

    ### Distance Table### Example

Consider the code C= {(0,0,0,0),(0,0,1,1),(0,1,0,1),(0,1,1,0),
(1,0,0,1),(1,0,1,0),(1,1,0,0),(1,1,1,1)}⊆A^4.

The codewords of the binary code
from Example 3.2. have the Hamming distances (pic) and the minimum distance is d(C) = 2. In contrast to that there are original words
(for example (0,0,1) and (0,1,1)) that diﬀer only in one position. Hence the encoding
enlarged the distance between the words.
    """
    
    # Calculate distances
    n = len(codewords)
    distances = np.zeros((n, n), dtype=int)
    
    for i in range(n):
        for j in range(n):
            distances[i,j] = hamming_distance(codewords[i], codewords[j])
    
    # Create HTML content with LaTeX-like formatting
    html_content = '''
    <div class="latex-container">
        <div class="table-title">Table 1: Hamming Distances Between Codewords</div>
        <table class="hamming-table">
    '''
    
    # Header row with codewords
    html_content += '<tr><th>C</th>'
    for cw in codewords:
        html_content += f'<th>({",".join(map(str, cw))})</th>'
    html_content += '</tr>'
    
    # Table content
    for i, cw1 in enumerate(codewords):
        html_content += f'<tr><th>({",".join(map(str, cw1))})</th>'
        for j, _ in enumerate(codewords):
            html_content += f'<td>{distances[i,j]}</td>'
        html_content += '</tr>'
    
    html_content += '''
        </table>
        <div class="min-distance">
    '''
    
    # Display minimum distance
    min_dist = np.min(distances[distances > 0])
    html_content += f'Minimum distance d(C) = {min_dist}</div></div>'
    
    display(HTML(html_content))


def create_repetition_code_section():
    """
    basic content:

    ### Repitition code

    C= {(0,0,0,0,0,0),(0,1,0,1,0,1),(1,0,1,0,1,0),(1,1,1,1,1,1)}
    has minimum distance d(C) = 3 and is a 2-error-detecting and 1-error-correcting
    code. But when the codeword c= (0,0,0,0,0,0) is sent and x= (1,1,0,0,0,0)
    is received, 2 errors have occurred and Hamming decoding yields nevertheless
    the sent codeword c.
    """
    
    html_content = """
    <div class="latex-container">
        <div class="section-title">3-Repetition Code</div>
        
        <div class="content-box">
            <div class="definition-box">
                <p><strong>Code Construction:</strong></p>
                <p>Each bit is repeated 3 times in alternating positions:</p>
                
                <div style="display: flex; justify-content: center; align-items: center; margin: 20px 0;">
                    <table class="encoding-table">
                        <tr>
                            <th>Data Word</th>
                            <th></th>
                            <th>Codeword</th>
                            <th style="padding-left: 20px;">Pattern</th>
                        </tr>
                        <tr>
                            <td>(0,0)</td>
                            <td class="arrow">→</td>
                            <td>(0,0,0,0,0,0)</td>
                            <td style="padding-left: 20px; color: #666;">
                                <span style="color: #2196F3">(0_0)</span> repeated 3 times
                            </td>
                        </tr>
                        <tr>
                            <td>(0,1)</td>
                            <td class="arrow">→</td>
                            <td>(0,1,0,1,0,1)</td>
                            <td style="padding-left: 20px; color: #666;">
                                <span style="color: #2196F3">(0_1)</span> repeated 3 times
                            </td>
                        </tr>
                        <tr>
                            <td>(1,0)</td>
                            <td class="arrow">→</td>
                            <td>(1,0,1,0,1,0)</td>
                            <td style="padding-left: 20px; color: #666;">
                                <span style="color: #2196F3">(1_0)</span> repeated 3 times
                            </td>
                        </tr>
                        <tr>
                            <td>(1,1)</td>
                            <td class="arrow">→</td>
                            <td>(1,1,1,1,1,1)</td>
                            <td style="padding-left: 20px; color: #666;">
                                <span style="color: #2196F3">(1_1)</span> repeated 3 times
                            </td>
                        </tr>
                    </table>
            </div>
            
                <div style="display: flex; justify-content: space-around; align-items: center; margin: 20px 0;">
                    <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 8px;">
                        <strong>Properties</strong>
                        <ul style="text-align: left; margin: 5px 0;">
                            <li>Minimum distance: d(C) = 3</li>
                            <li>2-error-detecting</li>
                            <li>1-error-correcting</li>
                </ul>
                    </div>
                </div>
            </div>

            <div class="example-box">
                <div class="example-title">Interesting Case</div>
                
                <div class="communication-diagram">
                    <div class="sender">
                        <strong>Sent Codeword</strong>
                        <div class="message">c = (0,0,0,0,0,0)</div>
                        <div class="note">Encoding of (0,0)</div>
                    </div>
                    
                    <div class="channel">
                        <div class="error">⚡ Two Errors</div>
                    </div>
                    
                    <div class="receiver">
                        <strong>Received Word</strong>
                        <div class="message error-message">x = (1,1,0,0,0,0)</div>
                        <div class="note">First two bits flipped</div>
                    </div>
                </div>

                <div style="display: flex; justify-content: center; align-items: center; margin: 20px 0;">
                    <div style="text-align: center;">
                        <strong>Analysis</strong>
                        <div style="display: flex; align-items: center; margin-top: 10px;">
                            <div style="background: #e3f2fd; padding: 10px; border-radius: 8px;">
                                <div>Errors</div>
                                <div class="message">2 bits flipped</div>
                            </div>
                            <div style="margin: 0 15px;">→</div>
                            <div style="background: #fff3e0; padding: 10px; border-radius: 8px;">
                                <div>Expected</div>
                                <div>Decoding failure</div>
                            </div>
                            <div style="margin: 0 15px;">→</div>
                            <div style="background: #e8f5e9; padding: 10px; border-radius: 8px;">
                                <div>Actual</div>
                                <div class="message">Decodes to (0,0)</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="note">
                <p><strong>Important Observation:</strong></p>
                <ul>
                    <li>Each 2-bit word is encoded by repeating it 3 times</li>
                    <li>The code is only guaranteed to correct 1 error</li>
                    <li>However, in this case it correctly decoded despite 2 errors</li>
                    <li>This demonstrates that error-correction capabilities are minimum guarantees</li>
                    <li>Sometimes codes can perform better than their guaranteed minimum</li>
                </ul>
            </div>
        </div>
    </div>
    """
    
    display(HTML(html_content))


def create_linear_codes_section():
    """
    basic content:

    ## Linear codes

    Introducing structure in a code allows us to find codewords with ease. Also, encoding becomes easy.
    Linear codes allow us to form codewords using less computational capacity. Linear codes are codes that
    form a subspace of the field {0,1}n. A subspace of a field is a subset which is closed under addition
    (mod two for {0,1}n) i.e. x,y∈C= ⇒ x+ y∈C.

    Since linear codes are a subspace, the codes can be represented by the basis of the subspace (in
    {0,1}n). Therefore forming a matrix Gk×n from the basis vectors we have,
    C= {xT G,x∈{0,1}k }

    Here G is called the generator matrix of C. The size of the code is M = 2k. Thus a linear code can be
    written in terms of its length n, dimension k, and minimum distance d as [n,k,d].
    An [n,k,d] linear code is a subspace of a vector space and also an (n,2k,d) code. It is given by a
    k×n generator matrix.

    Linear codes are formed by linear mapping of a k-bit vector to an n-bit vector (codewords).

    φ: {0,1}k →{0,1}n

    Codes are the sets C= {φ(x) : x ∈{0,1}k }. For a k length vector x ∈{0,1}k, the corresponding
    codeword is calculated by xT G, where G ∈{0,1}n×k is the generator matrix.

    x: k×1 vector
    G: k×n matrix
    xT G: 1×n vector

    For a linear code C= {xT G: x∈{0,1}k }, we have that: ∀y1,y2 ∈C ⇒y1 + y2 ∈C
    A linear code of size k, length n and minimum distance d is represented as [n,k,d]-code.
    """
    
    html_content = """
    <div class="latex-container">
        <div class="section-title">Linear Codes</div>
        
        <div class="content-box">
            <div class="definition-box">
                <p><strong>Introduction:</strong></p>
                <p>Linear codes introduce structure that enables efficient codeword discovery and encoding processes. 
                These codes allow us to form codewords using less computational capacity.</p>
                
                <p><strong>Definition:</strong> A linear code is a subspace of {0,1}ⁿ with the following property:</p>
                <ul>
                    <li>If x,y ∈ C, then x + y ∈ C (addition mod 2)</li>
                    <li>This structure allows efficient encoding and decoding</li>
                </ul>
        </div>

        <div class="example-box">
                <div class="example-title">Linear Mapping</div>
                <p>Linear codes are formed by mapping:</p>
                <div style="text-align: center; padding: 10px;">
                    <span class="math">φ: {0,1}ᵏ → {0,1}ⁿ</span>
                </div>
                <p>The code set is: <span class="math">C = {φ(x) : x ∈ {0,1}ᵏ}</span></p>
        </div>

        <div class="example-box">
                <div class="example-title">Generator Matrix Construction</div>
                
                <div style="display: flex; justify-content: space-around; align-items: center; margin: 20px 0;">
                    <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 8px;">
                        <strong>Basis Vectors</strong>
                        <div class="message">
                            v₁ = (1,0,0,1,1)<br>
                            v₂ = (0,1,0,1,0)<br>
                            v₃ = (0,0,1,0,1)
                        </div>
                    </div>
                    <div style="margin: 0 15px;">→</div>
                    <div style="text-align: center; padding: 15px; background: #fff3e0; border-radius: 8px;">
                        <strong>Generator Matrix G</strong>
                        <div class="message">
                            G = [1 0 0 1 1]<br>
                            &nbsp;&nbsp;&nbsp;&nbsp;[0 1 0 1 0]<br>
                            &nbsp;&nbsp;&nbsp;&nbsp;[0 0 1 0 1]
                        </div>
                    </div>
        </div>

        <div class="example-box">
                    <div class="example-title">Encoding Process</div>
                    <div style="display: flex; justify-content: center; align-items: center; margin: 10px 0;">
                        <div style="text-align: center; padding: 10px; background: #e3f2fd; border-radius: 8px;">
                            <strong>Data Word</strong>
                            <div class="message">x = (1,1,0)</div>
                            <div class="note">k×1 vector</div>
                        </div>
                        <div style="margin: 0 15px;">→</div>
                        <div style="text-align: center; padding: 10px; background: #fff3e0; border-radius: 8px;">
                            <strong>Computation</strong>
                            <div class="message">xᵀG = (1·v₁ + 1·v₂ + 0·v₃)</div>
                            <div class="note">Matrix multiplication</div>
                        </div>
                        <div style="margin: 0 15px;">→</div>
                        <div style="text-align: center; padding: 10px; background: #e8f5e9; border-radius: 8px;">
                            <strong>Codeword</strong>
                            <div class="message">(1,1,0,0,1)</div>
                            <div class="note">1×n vector</div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="definition-box">
                <p><strong>Code Parameters [n,k,d]:</strong></p>
                <ul>
                    <li><span class="key-term">n</span>: Length of codewords</li>
                    <li><span class="key-term">k</span>: Dimension (number of basis vectors)</li>
                    <li><span class="key-term">d</span>: Minimum distance</li>
                    <li>Code size: M = 2ᵏ codewords</li>
            </ul>
                <p class="note">An [n,k,d] linear code is both a subspace of a vector space and an (n,2ᵏ,d) code.</p>
        </div>

            <div class="note">
                <p><strong>Key Properties:</strong></p>
                <ul>
                    <li>All codewords are formed as linear combinations of basis vectors</li>
                    <li>Generator matrix G has dimensions k × n</li>
                    <li>Each k-bit message maps to an n-bit codeword</li>
                    <li>The mapping is linear: φ(x) = xᵀG</li>
                    <li>For any y₁,y₂ ∈ C: y₁ + y₂ ∈ C (closure under addition)</li>
                </ul>
    </div>
        </div>
    </div>
    """
    
    display(HTML(html_content))
   

def show_generator_matrix_example():
    """
    basic content:

    ### Example

    Suppose, a generator matrix G is given by:

    G= [1 0 0 1 0 1,
    0 1 0 1 1 0,
    0 0 1 1 1 1,
    ]

    The encoding is given by just multiplying with the generator matrix:
    000 →000000
    001 →001111
    010 →010110
    011 →011001
    100 →100101
    101 →101010
    110 →110011
    111 →111100
    Note that, the parameters of the code ([6,3,3]) remain same if we change the order of labeling. In
    error-correcting codes it does not matter what the particular map between the messages and codewords
    is, the only geometry that matters is that of the codewords.
    Our objective is to construct codes of arbitrary length that correct any given number of errors with
    simple encoding and decoding algorithms.
    """
    
    html_content = """
    <div class="latex-container">
        <div class="section-title">Generator Matrix Example: [6,3,3] Code</div>
        
        <div class="content-box">
            <div class="definition-box">
                <p><strong>Generator Matrix G:</strong></p>
                <div class="matrix-display">
                    G = [<br>
                    1 0 0 1 0 1<br>
                    0 1 0 1 1 0<br>
                    0 0 1 1 1 1<br>
                    ]
                </div>
                <p class="note">This is a [6,3,3] code: length=6, dimension=3, min distance=3</p>
            </div>
            
            <div class="example-box">
                <div class="example-title">Complete Encoding Table</div>
                <div style="display: flex; justify-content: center; margin: 20px 0;">
            <table class="encoding-table">
                <tr>
                            <th>Message</th>
                    <th></th>
                            <th>Codeword</th>
                            <th style="padding-left: 20px;">Computation</th>
                </tr>
                        <tr>
                            <td>000</td>
                            <td class="arrow">→</td>
                            <td>000000</td>
                            <td style="padding-left: 20px; color: #666;">0·r₁ + 0·r₂ + 0·r₃</td>
                        </tr>
                        <tr>
                            <td>001</td>
                            <td class="arrow">→</td>
                            <td>001111</td>
                            <td style="padding-left: 20px; color: #666;">r₃</td>
                        </tr>
                        <tr>
                            <td>010</td>
                            <td class="arrow">→</td>
                            <td>010110</td>
                            <td style="padding-left: 20px; color: #666;">r₂</td>
                        </tr>
                        <tr>
                            <td>011</td>
                            <td class="arrow">→</td>
                            <td>011001</td>
                            <td style="padding-left: 20px; color: #666;">r₂ + r₃</td>
                        </tr>
                        <tr>
                            <td>100</td>
                            <td class="arrow">→</td>
                            <td>100101</td>
                            <td style="padding-left: 20px; color: #666;">r₁</td>
                        </tr>
                        <tr>
                            <td>101</td>
                            <td class="arrow">→</td>
                            <td>101010</td>
                            <td style="padding-left: 20px; color: #666;">r₁ + r₃</td>
                        </tr>
                        <tr>
                            <td>110</td>
                            <td class="arrow">→</td>
                            <td>110011</td>
                            <td style="padding-left: 20px; color: #666;">r₁ + r₂</td>
                        </tr>
                        <tr>
                            <td>111</td>
                            <td class="arrow">→</td>
                            <td>111100</td>
                            <td style="padding-left: 20px; color: #666;">r₁ + r₂ + r₃</td>
                        </tr>
            </table>
                </div>
                <p class="note">r₁, r₂, r₃ represent the rows of G</p>
            </div>

            <div class="important-note">
                <p><strong>Key Properties:</strong></p>
                <ul>
                    <li>The code parameters [6,3,3] remain unchanged regardless of labeling order</li>
                    <li>The geometric relationship between codewords matters more than the specific mapping</li>
                    <li>This code can detect 2 errors and correct 1 error</li>
                </ul>
            </div>
            
            <div class="note">
                <p><strong>Objective:</strong> This example demonstrates how we can construct codes of arbitrary length 
                that correct any given number of errors while maintaining simple encoding and decoding algorithms.</p>
            </div>
        </div>
    </div>
    """
    
    display(HTML(html_content))


def create_dual_codes_section():
  
    
    html_content = """
    <div class="latex-container">
        <div class="section-title">Dual Codes and Parity Check Matrix</div>
        
        <div class="definition-box">
            <p><strong>Linear Code Structure:</strong></p>
            <p>Each linear code is the linear subspace spanned by G, where rows of G are bases of this subspace. 
            This is why G is called a generator matrix.</p>
        </div>

        <div class="theorem">
            <p><strong>Dual Subspace Definition:</strong></p>
            <p>The dual code of C is defined as:</p>
            <div class="equation">
                C<sup>⊥</sup> = {z | ⟨x,z⟩ = 0, ∀x ∈ C}
            </div>
            <p>where ⟨x,z⟩ is the inner product of two vectors:</p>
            <div class="equation">
                For x = [x₁,x₂,...,xₙ]<sup>T</sup> and z = [z₁,z₂,...,zₙ]<sup>T</sup><br>
                ⟨x,z⟩ = x<sup>T</sup>z = Σ<sub>i=1</sub><sup>n</sup> x<sub>i</sub>z<sub>i</sub>
            </div>
            <p class="note"><em>Note: Each operation is modulo 2</em></p>
        </div>

        <div class="important-note">
            <p><strong>Key Properties:</strong></p>
            <ul>
                <li>Vectors in the dual space are called dual code C<sup>⊥</sup></li>
                <li>Linear codes (primal) and dual codes may share codewords</li>
                <li>It's possible that an element of C<sup>⊥</sup> is in C</li>
                <li>When C = C<sup>⊥</sup>, we call C a self-dual code</li>
            </ul>
        </div>

        <div class="definition-box">
            <p><strong>Dimensional Properties:</strong></p>
            <ul>
                <li>If original subspace has dimension k</li>
                <li>Then dual subspace has dimension (n-k)</li>
            </ul>
        </div>

        <div class="theorem">
            <p><strong>Parity Check Matrix:</strong></p>
            <p>The generator matrix of the dual code is called the parity-check matrix.</p>
            <p>The minimum distance of the dual code (d<sup>⊥</sup>) has no clear relation to the original code's minimum distance (d).</p>
        </div>

        
    </div>
    """
    
    display(HTML(html_content))


def create_dual_code_examples():

    """
    basic content:

    ## Dual codes and Parity Check Matrix

Each linear code is the linear subspace spanned by G, which means rows of Gare bases of this subspace.
That's why we call G a generator matrix. Each linear subspace has a dual subspace. It(dual subspace)
is the set of the vectors that are orthogonal to the vectors of linear codes (spanned by the row space of
the generator matrix). The dual code of C is

C⊥
= {z|⟨x,z⟩= 0,∀x∈C}

⟨x,z⟩is the inner product of two vectors. Say x = [x1,x2,...,xn]T and z = [z1,z2,...,zn]T then
⟨x,z⟩= xT z=
n
i=1 xizi. (Each operation is modulo 2).

Vectors in the dual space are called dual code C⊥. The linear codes (primal) and dual codes may
have same codewords. It is possible that an element of C⊥is in C. In particular, it is possible to have

C= C⊥. In this case we call code C a self-dual code. If the original subspace has dimension k, then the
dimension of the dual subspace is (n−k).
We call the generator matrix of the dual code, parity-check matrix. The minimum distance of the dual
code of a code with minimum distance dis denoted by by d⊥. In general, the relation between dand d⊥
is unclear.

    """

    
    
    html_content = """
    <div class="latex-container">
        <div class="section-title">Examples of Dual Codes and Parity Check Matrices</div>
        
        <div class="example-box">
            <h3>Example 1: [7,4,3] Hamming Code</h3>
            <p>Consider the generator matrix G:</p>
            <div class="matrix-display">
                G = [<br>
                1 0 0 0 1 1 1<br>
                0 1 0 0 1 1 0<br>
                0 0 1 0 1 0 1<br>
                0 0 0 1 0 1 1<br>
                ]
            </div>
            
            <p>The corresponding parity check matrix H:</p>
            <div class="matrix-display">
                H = [<br>
                1 1 1 0 1 0 0<br>
                1 1 0 1 0 1 0<br>
                1 0 1 1 0 0 1<br>
                ]
            </div>
            
            <div class="calculation">
                <p><strong>Verification:</strong> GH<sup>T</sup> = 0 (mod 2)</p>
                <p>Any codeword c = xG satisfies cH<sup>T</sup> = 0</p>
            </div>
        </div>
        <div class="example-box">
            <div class="example-title">Verification Example</div>
            
            <div style="display: flex; justify-content: space-around; align-items: center; margin: 20px 0;">
                <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 8px;">
                    <strong>Take codeword from C</strong>
                    <div class="message">
                        x = (1,0,0,0,1,1,1)
                    </div>
                    <div class="note">x = (1,0,0,0)G</div>
                </div>
                
                <div style="margin: 0 15px;">×</div>
                
                <div style="text-align: center; padding: 15px; background: #fff3e0; border-radius: 8px;">
                    <strong>Take dual codeword from C<sup>⊥</sup></strong>
                    <div class="message">
                        z = (1,1,1,0,1,0,0)
                    </div>
                    <div class="note">First row of H</div>
                </div>
            </div>

            <div class="calculation">
                <p><strong>Inner Product Calculation:</strong></p>
                <div style="display: flex; justify-content: center; align-items: center; margin: 10px 0;">
                    <div style="text-align: center; padding: 10px; background: #f5f5f5; border-radius: 8px;">
                        ⟨x,z⟩ = (1·1 + 0·1 + 0·1 + 0·0 + 1·1 + 1·0 + 1·0) mod 2
                    </div>
                </div>
                <div style="display: flex; justify-content: center; gap: 20px; margin: 10px 0;">
                    <div>= (1 + 0 + 0 + 0 + 1 + 1 + 1) mod 2</div>
                    <div>= 4 mod 2</div>
                    <div>= 0</div>
                </div>
            </div>

            <div class="note">
                <p><strong>Key Points:</strong></p>
                <ul>
                    <li>Every codeword from C is orthogonal to every codeword from C<sup>⊥</sup></li>
                    <li>Inner product is always 0 (mod 2)</li>
                    <li>This property holds for all possible combinations of codewords from C and C<sup>⊥</sup></li>
                </ul>
            </div>
        </div>
        <div class="example-box">
            <h3>Example 2: Self-Dual Code [8,4,4]</h3>
            <p>A self-dual extended Hamming code with generator matrix:</p>
            <div class="matrix-display">
                G = [<br>
                1 0 0 0 1 1 1 0<br>
                0 1 0 0 1 1 0 1<br>
                0 0 1 0 1 0 1 1<br>
                0 0 0 1 0 1 1 1<br>
                ]
            </div>
            
            <div class="note">
                <p>This code is self-dual because:</p>
                <ul>
                    <li>G generates both C and C<sup>⊥</sup></li>
                    <li>Every codeword has even weight</li>
                    <li>Any two codewords have even overlap</li>
                </ul>
            </div>
        </div>

        
    </div>
    """
    
    display(HTML(html_content))



def create_minimal_codewords_section():
    """
    basic content:

    ## Minimal codewords

    the support of v is given by supp(v) = {i : vi =
    0, 1 ≤ i ≤ n}. A vector v2 covers a vector v1 if the support of v2
    contains that of v1.
    A non-zero codeword of C is called minimal vector
    if its support does not properly contain the support of another non-
    zero codeword

    A codeword c ∈ C is called a minimal codeword
    if its first coordinate is 1 and covers no other codeword whose first
    coordinate is 1
    """

    html_content = """
    <div class="latex-container">
        <div class="section-title">Minimal Codewords</div>
        
        <div class="content-box">
            <div class="definition-box">
                <p><strong>Core Concepts:</strong></p>
                <div style="display: flex; justify-content: space-around; align-items: flex-start; margin: 20px 0;">
                    <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 8px; flex: 1; margin: 0 10px;">
                        <strong>Support</strong>
                        <p class="math">supp(v) = {i : vᵢ ≠ 0}</p>
                        <div class="note">Positions of non-zero elements</div>
                    </div>
                    
                    <div style="text-align: center; padding: 15px; background: #fff3e0; border-radius: 8px; flex: 1; margin: 0 10px;">
                        <strong>Coverage</strong>
                        <p class="math">supp(v₁) ⊆ supp(v₂)</p>
                        <div class="note">v₂ covers v₁</div>
                    </div>
                    
                    <div style="text-align: center; padding: 15px; background: #e8f5e9; border-radius: 8px; flex: 1; margin: 0 10px;">
                        <strong>Minimality</strong>
                        <p>Two Types:</p>
                        <div class="note">
                            1. Minimal Vector<br>
                            2. Minimal Codeword
                        </div>
                    </div>
            </div>
        </div>

        <div class="example-box">
                <div class="example-title">Visual Example</div>
                
                <div style="display: flex; justify-content: center; align-items: center; margin: 20px 0;">
                    <table class="encoding-table">
                        <tr>
                            <th>Vector</th>
                            <th>Binary Form</th>
                            <th>Support</th>
                            <th>Minimal Vector?</th>
                            <th>Minimal Codeword?</th>
                        </tr>
                        <tr>
                            <td>c₁</td>
                            <td>(1,1,0,0,0)</td>
                            <td>{1,2}</td>
                            <td style="color: #4CAF50;">✓ Yes</td>
                            <td style="color: #4CAF50;">✓ Yes</td>
                        </tr>
                        <tr>
                            <td>c₂</td>
                            <td>(1,1,1,0,0)</td>
                            <td>{1,2,3}</td>
                            <td style="color: #f44336;">✗ No</td>
                            <td style="color: #f44336;">✗ No</td>
                        </tr>
                        <tr>
                            <td>c₃</td>
                            <td>(0,1,1,0,0)</td>
                            <td>{2,3}</td>
                            <td style="color: #4CAF50;">✓ Yes</td>
                            <td style="color: #f44336;">✗ No</td>
                        </tr>
                    </table>
            </div>
            
                <div style="display: flex; justify-content: space-around; align-items: flex-start; margin: 20px 0;">
                    <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 8px;">
                        <strong>Minimal Vector Criteria</strong>
                        <div class="note">
                            Support doesn't contain<br>
                            another codeword's support
                        </div>
            </div>
            
                    <div style="text-align: center; padding: 15px; background: #fff3e0; border-radius: 8px;">
                        <strong>Support Relationships</strong>
                        <div style="margin-top: 10px;">
                            <span class="math">{1,2}</span> ⊆ <span class="math">{1,2,3}</span>
                            <div class="note">c₂ covers c₁</div>
                        </div>
                        <div style="margin-top: 10px;">
                            <span class="math">{2,3}</span> ⊆ <span class="math">{1,2,3}</span>
                            <div class="note">c₂ covers c₃</div>
                        </div>
                    </div>

                    <div style="text-align: center; padding: 15px; background: #e8f5e9; border-radius: 8px;">
                        <strong>Minimal Codeword Criteria</strong>
                        <div class="note">
                            1. First coordinate is 1<br>
                            2. Doesn't cover other codewords<br>
                            with first coordinate 1
                        </div>
                    </div>
                </div>
            </div>

            <div class="note">
                <p><strong>Key Properties:</strong></p>
                <ul>
                    <li>A minimal vector's support cannot contain another non-zero codeword's support</li>
                    <li>A minimal codeword must have 1 in its first coordinate</li>
                    <li>A minimal codeword cannot cover other codewords with first coordinate 1</li>
                    <li>c₃ is a minimal vector but not a minimal codeword (first coordinate is 0)</li>
                    <li>c₁ is both a minimal vector and a minimal codeword</li>
                </ul>
            </div>
        </div>
    </div>
    """
    
    display(HTML(html_content))


def create_secret_sharing_section():
    """
    basic content:

    # 2. Secret Sharing

    A secret-sharing scheme (SSS) involves a dealer who detains a secret.
    This dealer distributes its secret to a set of participants (also called
    users or shareholders) in order that each party holds a share (or
    fragment) of that secret. Some special subsets of participants can
    reconstruct the secret while the other cannot. The groups that can
    reconstruct the secret are called qualiﬁed (or sometimes authorized)
    and the other groups are called rejected (or sometimes forbidden).

    In a secret sharing scheme, a secret "s" is distributed among many users. The information that a
    user gets is called a share. We deﬁne a secret sharing scheme such that for some sets of the users, when
    they get together, the secret is revealed and for some sets of users, the secret can't be revealed from their
    shares. For the rest of the lecture, we will assume the following notation : Let a secret s be distributed
    among n users.

    ## Threshold Secret Sharing Scheme

    If the secret s is distributed such that the following conditions hold, then it is called Threshold secret
    sharing scheme.
    1 If any set of k or more users get together, then the secret will be revealed.
    2 For all sets of k − 1 or less users, the secret will not be revealed.
    It is denoted by (n, k)-Threshold scheme where n is the number of users and k is the threshold.

    ## Access and Block Structures

    Let [n] = {1, 2, . . . , n} and 2[n] be power set of [n].
    Access Structure A ⊆ 2[n] is such that any set a ∈ A can reveal secret s.
    For eg. A = {{1, 2}, {2, 3, 4}}, then when users 1, 2 or users 2, 3, 4 get together, they can reveal s.
    Block Structure B ⊆ 2[n] is such that any set b ∈ B cannot reveal the secret s.
    """
    
    html_content = """
    <div class="latex-container">
        <div class="section-title">Secret Sharing</div>
        
        <div class="content-box">
        <div class="definition-box">
                <p><strong>Basic Concept:</strong></p>
                <p>A secret-sharing scheme (SSS) involves a dealer who detains a secret. This dealer distributes its secret 
                to a set of participants (also called users or shareholders) in order that each party holds a share (or fragment) 
                of that secret.</p>
                
                <div style="display: flex; justify-content: space-around; align-items: center; margin: 20px 0;">
                    <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 8px;">
                        <strong>Dealer</strong>
                        <div class="message">Secret s</div>
                    </div>
                    <div style="margin: 0 15px;">→</div>
                    <div style="text-align: center; padding: 15px; background: #fff3e0; border-radius: 8px;">
                        <strong>Shares</strong>
                        <div class="message">
                            Share₁<br>
                            Share₂<br>
                            ⋮<br>
                            Shareₙ
                        </div>
                    </div>
                    <div style="margin: 0 15px;">→</div>
                    <div style="text-align: center; padding: 15px; background: #e8f5e9; border-radius: 8px;">
                        <strong>Participants</strong>
                        <div class="message">n users</div>
                    </div>
        </div>

                <div class="note">
                    <p>In a secret sharing scheme, a secret "s" is distributed among many users. The information that a
                    user gets is called a share. We define a secret sharing scheme such that for some sets of the users, when
                    they get together, the secret is revealed and for some sets of users, the secret can't be revealed from their
                    shares.</p>
                </div>
            </div>

            <div class="example-box">
                <div class="example-title">Threshold Secret Sharing Scheme</div>

        <div class="definition-box">
                    <p><strong>Definition:</strong></p>
                    <p>If the secret s is distributed such that the following conditions hold, then it is called Threshold secret
                    sharing scheme:</p>
        </div>

                <div style="display: flex; justify-content: space-around; align-items: flex-start; margin: 20px 0;">
                    <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 8px; flex: 1; margin: 0 10px;">
                        <strong>Condition 1</strong>
                        <div class="message">k or more users</div>
                        <div class="note" style="color: #4CAF50;">Secret will be revealed</div>
                    </div>
                    
                    <div style="text-align: center; padding: 15px; background: #fff3e0; border-radius: 8px; flex: 1; margin: 0 10px;">
                        <strong>Condition 2</strong>
                        <div class="message">k-1 or fewer users</div>
                        <div class="note" style="color: #f44336;">Secret will not be revealed</div>
                    </div>
        </div>

        <div class="example-box">
                    <div class="example-title">(n,k)-Threshold Scheme Parameters</div>
                    <div style="display: flex; justify-content: space-around; align-items: center; margin: 20px 0;">
                        <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 8px;">
                            <strong>n</strong>
                            <div class="message">Total number of users</div>
                        </div>
                        
                        <div style="text-align: center; padding: 15px; background: #fff3e0; border-radius: 8px;">
                            <strong>k</strong>
                            <div class="message">Threshold value</div>
                            <div class="note">Minimum users needed</div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="example-box">
                <div class="example-title">Example Scenarios</div>
                <div style="display: flex; justify-content: space-around; align-items: flex-start; margin: 20px 0;">
                    <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 8px;">
                        <strong>(5,3)-Threshold Scheme</strong>
                        <div class="message">
                            Success: Any 3+ users<br>
                            Failure: Any 2 or fewer
                        </div>
                    </div>
                    
                    <div style="text-align: center; padding: 15px; background: #fff3e0; border-radius: 8px;">
                        <strong>Sample Groups</strong>
                        <div style="text-align: left;">
                            ✓ Users {1,2,3}<br>
                            ✓ Users {2,3,4,5}<br>
                            ✗ Users {1,2}<br>
                            ✗ Users {4,5}
                        </div>
                    </div>
                </div>
            </div>

            <div class="example-box">
                <div class="example-title">Access and Block Structures</div>
                <p>Let [n] = {1, 2, . . . , n} and 2[n] be power set of [n].</p>
                
                <div style="display: flex; justify-content: space-around; align-items: flex-start; margin: 20px 0;">
                    <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 8px;">
                        <strong>Access Structure (A)</strong>
                        <div class="message">A ⊆ 2[n]</div>
                        <div class="example" style="margin-top: 10px;">
                            Example: A = {{1,2}, {2,3,4}}<br>
                            Users 1,2 or 2,3,4 can reveal s
                        </div>
                        <div class="note">Any set a ∈ A can reveal secret s</div>
                    </div>
                    
                    <div style="text-align: center; padding: 15px; background: #fff3e0; border-radius: 8px;">
                        <strong>Block Structure (B)</strong>
                        <div class="message">B ⊆ 2[n]</div>
                        <div class="note">Any set b ∈ B cannot reveal s</div>
                    </div>
                </div>
            </div>

            <div class="note">
                <p><strong>Group Classifications:</strong></p>
                <ul>
                    <li>Qualified (Authorized) Groups:
                        <ul>
                            <li>Can reconstruct the secret</li>
                            <li>Part of Access Structure A</li>
            </ul>
                    </li>
                    <li>Rejected (Forbidden) Groups:
                        <ul>
                            <li>Cannot reconstruct the secret</li>
                            <li>Part of Block Structure B</li>
                        </ul>
                    </li>
            </ul>
        </div>
        </div>
    </div>
    """
    
    display(HTML(html_content))




def create_massey_section_1():
    """
    basic content:
    # 3. Massey's Secret Sharing Scheme

    In 1993, James Massey showed that a secret-sharing scheme can be constructed using a linear code C. He
    introduced the notion of minimal codewords of a code and pointed
    out the relationship between access structures and minimal code-
    words of C⊥.
    """
    
    html_content = """
    <div class="latex-container">
        <div class="section-title">Massey's Secret Sharing Scheme</div>
        
        <div class="content-box">
            <div class="definition-box">
                <p><strong>Historical Context:</strong></p>
                <div style="display: flex; justify-content: space-around; align-items: center; margin: 20px 0;">
                    <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 8px;">
                        <strong>Year</strong>
                        <div class="message">1993</div>
        </div>

                    <div style="text-align: center; padding: 15px; background: #fff3e0; border-radius: 8px;">
                        <strong>Author</strong>
                        <div class="message">James Massey</div>
                    </div>
                </div>
        </div>

            <div class="theorem-box">
                <p><strong>Key Innovation:</strong></p>
                <div style="display: flex; justify-content: space-around; align-items: flex-start; margin: 20px 0;">
                    <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 8px; flex: 1; margin: 0 10px;">
                        <strong>Construction</strong>
                        <div class="message">Secret sharing using linear code C</div>
                    </div>
                    
                    <div style="text-align: center; padding: 15px; background: #fff3e0; border-radius: 8px; flex: 1; margin: 0 10px;">
                        <strong>Concept</strong>
                        <div class="message">Minimal codewords</div>
                    </div>
                    
                    <div style="text-align: center; padding: 15px; background: #e8f5e9; border-radius: 8px; flex: 1; margin: 0 10px;">
                        <strong>Relationship</strong>
                        <div class="message">Access structures ↔ Minimal codewords of C<sup>⊥</sup></div>
                    </div>
                </div>
            </div>

            <div class="note">
                <p><strong>Significance:</strong></p>
                <ul>
                    <li>Connected coding theory with secret sharing</li>
                    <li>Introduced new theoretical framework</li>
                    <li>Established relationship between:
                        <ul>
                            <li>Access structures in secret sharing</li>
                            <li>Minimal codewords in dual codes</li>
                        </ul>
                    </li>
            </ul>
        </div>
        </div>
    </div>
    """
    
    display(HTML(html_content))

def create_massey_section_2():
    """
    basic content:
    The construction uses an [N = n + 1, k, d] linear code C
over Fq (all the codes considered in this chapter are deﬁned over
Fq). Let G = (g0, g1, . . . , gn) be a generator matrix of C (it is a
k × (n + 1) matrix). The secret is denoted s ∈ Fq and the participants
are P1, P2, . . . , Pn.

The dealer computes the shares by randomly choosing a vector
u = (u0, . . . , uk−1) ∈ Fk
q
such that
s = ug0.
In practice, the dealer can randomly select k − 1 coordinates and
then compute the kth in order to obtain the right property. Thus,
there are qk−1 possible such u. This vector u is seen as an information
vector and The dealer then treats u as an information vector and
computes the corresponding codeword
t = (ug0, ug1, ... , ugn-1) = (t0, t1, . . . , tn−1) = uG where t0 = s is the secret and the other coordinates are the shares.

He then gives ti to party Pi as share for each i ≥ 1.

If g0, gi1, gi2, ... , gim-1 are linearly dependent, then the secret can be computed from the shares:

g0 = c1gi1 + c2gi2 + ... + cmgim

where x1, x2, ... , xm are constants from Fq.

Solving the system and finding the x1, x2, ... , xm, we can find the secret s:

s = t0 = ug0 = u(x1gi1 + x2gi2 + ... + xmgim)

             = x1ugi1 + x2ugi2 + ... + xmugim

             = x1ti1 + x2ti2 + ... + xmtin
    

    """
    
    html_content = """
    <div class="latex-container">
        <div class="section-title">Construction of Massey's Scheme</div>
        
        <div class="content-box">
            <div class="definition-box">
                <p><strong>Code Parameters:</strong></p>
                <div style="display: flex; justify-content: space-around; align-items: center; margin: 20px 0;">
                    <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 8px;">
                        <strong>Linear Code C</strong>
                        <div class="message">N =[n + 1, k, d]</div>
                        <div class="note">Over field Fq</div>
        </div>

                    <div style="text-align: center; padding: 15px; background: #fff3e0; border-radius: 8px;">
                        <strong>Generator Matrix G</strong>
                        <div class="message">G = (g₀, g₁, ..., gₙ)</div>
                        <div class="note">k × (n + 1) matrix</div>
                    </div>
                </div>
        </div>

            <div class="example-box">
                <div class="example-title">Share Generation Process</div>
                <p>To construct a secret sharing scheme from C, we follow these steps:</p>
                
                <div style="display: flex; justify-content: space-around; align-items: flex-start; margin: 20px 0;">
                    <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 8px;">
                        <strong>Step 1: Choose Vector</strong>
                        <div class="message">u = (u₀, ..., uₖ₋₁) ∈ Fq ^k</div>
                        <div class="note">Such that s = ug₀</div>
                        <div class="note" style="font-size: 0.9em;">
                            • Choose k-1 coordinates randomly<br>
                            • Compute kth for desired secret<br>
                            • qᵏ⁻¹ possible choices for u
                        </div>
                    </div>
                    
                    <div style="text-align: center; padding: 15px; background: #fff3e0; border-radius: 8px;">
                        <strong>Step 2: Generate Codeword</strong>
                        <div class="message">t = uG = (ug₀, ug₁, ..., ugₙ)</div>
                        <div class="equation" style="margin: 10px 0;">
                            t = (ug₀, ug₁, ..., ugₙ₋₁)<br>
                            = (t₀, t₁, ..., tₙ₋₁)
                        </div>
                        <div class="note">
                            • t₀ = s (secret)<br>
                            • t₁, ..., tₙ (shares)<br>
                            • Encoding using G
                        </div>
                    </div>
                    
                    <div style="text-align: center; padding: 15px; background: #e8f5e9; border-radius: 8px;">
                        <strong>Step 3: Distribute</strong>
                        <div class="message">Give tᵢ to party Pᵢ</div>
                        <div class="note">
                            • For each i ≥ 1<br>
                            • Each party gets one share<br>
                            • t₀ is kept secret
                        </div>
                    </div>
                </div>
            </div>

            <div class="theorem-box">
                <div class="theorem-title">Secret Recovery</div>
                <p>When g₀, gᵢ₁, gᵢ₂, ..., gᵢₘ₋₁ are linearly dependent:</p>
                
                <div style="text-align: center; padding: 15px; background: #f5f5f5; border-radius: 8px; margin: 10px 0;">
                    <div class="equation">g₀ = x₁gᵢ₁ + x₂gᵢ₂ + ... + xₘgᵢₘ</div>
                    <div class="note">where x₁, x₂, ..., xₘ are constants from Fq</div>
                </div>

                <p><strong>By solving this equation, and finding the constant c₁, c₂, ..., cₘ, we can find the secret s:</strong></p>
                <div style="text-align: center; padding: 15px; background: #f5f5f5; border-radius: 8px; margin: 10px 0;">
                    <div class="equation">
                        s = t₀ = ug₀ = u(x₁gᵢ₁ + x₂gᵢ₂ + ... + xₘgᵢₘ)<br>
                        = x₁ugᵢ₁ + x₂ugᵢ₂ + ... + xₘugᵢₘ<br>
                        = x₁tᵢ₁ + x₂tᵢ₂ + ... + xₘtᵢₘ
                    </div>
                    <div class="note">Secret can be recovered from shares tᵢ₁, tᵢ₂, ..., tᵢₘ</div>
                </div>
            </div>
        </div>
    </div>
    """
    
    display(HTML(html_content))

def create_massey_section_3():
    """
    basic content:
    So we have the following proposition:

Proposition 1: Let G be a generator matrix of an [n, k; q] code C with generator matrix G = (g0, g1, . . . , gn). In the secret
sharing scheme based on C, a set of shares {ti1 , ti2 , . . . , tim } determine the secret
if and only if there is a codeword
(1, 0, . . . , 0, ci1 , 0, . . . , 0, cim , 0, . . . , 0) (1)
in the dual code C⊥, where cij != = 0 for at least one j, 1 ≤ i2 < . . . < im ≤ n − 1
and 1 ≤ m ≤ n − 1.


Proof:

Suppose that the set of shares {ti1 , ti2 , . . . , tim } determines the secret. Then g0, gi1, gi2, ... , gim are linearly dependent. So

g0 = x1gi1 + x2gi2 + ... + xmgim for at least one of x1, x2, ... , xm != 0  So we have 

g0 - x1gi1 - x2gi2 - ... - xmgim = 0 with inner product notation:

<g, (1, 0, ..., 0, -x1, 0, ..., 0, -x2, 0, ..., 0, -xm, 0, ..., 0)> = 0 

So we have a codeword (1, 0, ..., 0, -x1, 0, ..., 0, -x2, 0, ..., 0, -xm, 0, ..., 0) in the dual code C⊥.

Conversely, suppose that there is a codeword (1, 0, ..., 0, ci1 , 0, ..., 0, cim , 0, ..., 0) in the dual code C⊥. Then g0, gi1, gi2, ... , gim are linearly dependent. So

g0 = x1gi1 + x2gi2 + ... + xmgim

So the secret s can be computed from the shares {ti1 , ti2 , . . . , tim }.

    
    """
    
    html_content = """
    <div class="latex-container">
        <div class="section-title">Massey's Proposition</div>
        
        <div class="content-box">
            <div class="theorem-box">
                <div class="theorem-title">Proposition 1</div>
                <p>Let G be a generator matrix of an [n, k; q] code C with generator matrix G = (g₀, g₁, ..., gₙ). 
                In the secret sharing scheme based on C, a set of shares {tᵢ₁, tᵢ₂, ..., tᵢₘ} determine the secret
                if and only if there is a codeword</p>
                
                <div style="text-align: center; padding: 15px; background: #f5f5f5; border-radius: 8px; margin: 10px 0;">
                    <div class="equation">
                        (1, 0, ..., 0, cᵢ₁, 0, ..., 0, cᵢₘ, 0, ..., 0)
                    </div>
                    <div class="note">
                        in the dual code C<sup>⊥</sup>, where cᵢⱼ ≠ 0 for at least one j<br>
                        1 ≤ i₂ < ... < iₘ ≤ n-1 and 1 ≤ m ≤ n-1
                    </div>
                </div>
            </div>

            <div class="proof-box">
                <div class="proof-title">Proof</div>
                
                <div class="proof-part">
            <p><strong>Forward Direction:</strong></p>
                    <ol>
                        <li>If shares {tᵢ₁, tᵢ₂, ..., tᵢₘ} determine the secret, then g₀, gᵢ₁, gᵢ₂, ..., gᵢₘ are linearly dependent</li>
                        <li>Therefore: g₀ = x₁gᵢ₁ + x₂gᵢ₂ + ... + xₘgᵢₘ for at least one of x₁, x₂, ..., xₘ ≠ 0</li>
                        <li>This means: g₀ - x₁gᵢ₁ - x₂gᵢ₂ - ... - xₘgᵢₘ = 0</li>
                        <li>Using inner product notation:
                            <div class="equation">
                                ⟨g, (1, 0, ..., 0, -x₁, 0, ..., 0, -x₂, 0, ..., 0, -xₘ, 0, ..., 0)⟩ = 0
                            </div>
                        </li>
                        <li>Therefore we have a codeword (1, 0, ..., 0, -x₁, 0, ..., 0, -x₂, 0, ..., 0, -xₘ, 0, ..., 0) in C<sup>⊥</sup></li>
            </ol>
                </div>

                <div class="proof-part">
            <p><strong>Reverse Direction:</strong></p>
                    <ol>
                        <li>If there exists a codeword (1, 0, ..., 0, cᵢ₁, 0, ..., 0, cᵢₘ, 0, ..., 0) in C<sup>⊥</sup></li>
                        <li>Then g₀, gᵢ₁, gᵢ₂, ..., gᵢₘ are linearly dependent</li>
                        <li>Therefore: g₀ = x₁gᵢ₁ + x₂gᵢ₂ + ... + xₘgᵢₘ</li>
                        <li>Thus, the secret s can be computed from the shares {tᵢ₁, tᵢ₂, ..., tᵢₘ}</li>
            </ol>
        </div>
            </div>
        </div>
    </div>
    """
    
    display(HTML(html_content))

def create_massey_section_4():
    """
    basic content:
    
    From Proposition and the discussions above, it is clear that there is a
one-to-one correspondence between the set of minimal access sets and the set
of minimal codewords of the dual code C⊥.

In order to ﬁnd the set of qualiﬁed groups, it is enough to ﬁnd
the set of minimal qualiﬁed groups. In fact, Massey shows in [31]
that there is a one-to-one correspondence between the set of minimal
qualiﬁed groups and the set of minimal codewords of C⊥. Therefore,
searching for the access structure of the scheme means determining
the minimal codewords of C⊥. In other words, the set of groups A
such that

A = {Pi : i ∈ supp(c) : c is a minimal codeword of C⊥} is a spanning set for the set of qualiﬁed groups.
    """
    
    html_content = """
    <div class="latex-container">
        <div class="section-title">Correspondence Between Access Sets and Minimal Codewords</div>
        
        <div class="content-box">
            <div class="theorem-box">
                <div class="theorem-title">Key Result</div>
                <p>From the Proposition and previous discussions, there is a one-to-one correspondence between:</p>
                <div style="display: flex; justify-content: space-around; align-items: center; margin: 20px 0;">
                    <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 8px;">
                        <strong>Set of minimal access sets</strong>
                    </div>
                    <div style="margin: 0 15px;">↔</div>
                    <div style="text-align: center; padding: 15px; background: #fff3e0; border-radius: 8px;">
                        <strong>Set of minimal codewords of C<sup>⊥</sup></strong>
                    </div>
                </div>
            </div>

            <div class="definition-box">
                <p><strong>Finding Qualified Groups:</strong></p>
                <ul>
                    <li>It is sufficient to find the set of minimal qualified groups</li>
                    <li>Massey showed this correspondence in his work [31]</li>
                    <li>This reduces the problem to finding minimal codewords of C<sup>⊥</sup></li>
            </ul>
            </div>

            <div class="example-box">
                <div class="example-title">Access Structure Construction</div>
                <p>The set of qualified groups can be determined by:</p>
                
                <div style="text-align: center; padding: 15px; background: #f5f5f5; border-radius: 8px; margin: 10px 0;">
                    <div class="equation">
                        A = {Pᵢ : i ∈ supp(c) where c is a minimal codeword of C<sup>⊥</sup>}
                    </div>
                    <div class="note">This set A is a spanning set for all qualified groups</div>
                </div>

                <div style="display: flex; justify-content: space-around; align-items: flex-start; margin: 20px 0;">
                    <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 8px;">
                        <strong>Process</strong>
                        <div class="message">
                            1. Find C<sup>⊥</sup><br>
                            2. Find minimal codewords<br>
                            3. Get supports<br>
                            4. Map to participants
                        </div>
                    </div>
                    
                    <div style="text-align: center; padding: 15px; background: #fff3e0; border-radius: 8px;">
                        <strong>Result</strong>
                        <div class="message">
                            Complete access<br>
                            structure of the<br>
                            secret sharing scheme
                        </div>
                    </div>
                </div>
            </div>

            <div class="note">
                <p><strong>Practical Implications:</strong></p>
                <ul>
                    <li>The access structure is completely determined by C<sup>⊥</sup>'s minimal codewords</li>
                    <li>This provides an efficient way to identify all qualified groups</li>
                    <li>The correspondence simplifies the analysis of secret sharing schemes</li>
            </ul>
            </div>
        </div>
    </div>
    """
    
    display(HTML(html_content))

def create_example_section_example():
    """
    basic content:
    
    # 5. Example

Let C be a [6, 4, 2]-linear code over F5 with generator matrix

G =
⎛
⎜
⎜
⎜
⎝
1 0 0 0 4 0
0 1 0 0 4 1
1 0 1 0 3 1
0 0 0 1 0 4
⎞
⎟
⎟
⎟
⎠

and parity-check matrix

H =
(1 0 0 1 1 1
0 1 1 4 0 4
)


Suppose the secret is s = 3 ∈ F5. The dealer chooses u = (1123) and
computes the codeword t = uG = (312340). Thus, t0 is the secret
and the shares are t1 = 1, t2 = 2, t3 = 3, t4 = 4, t5 = 0. The dealer
then sends the share ti to participant pi. The set of codewords whose
ﬁrst coeﬃcient is 1 is


{(100111), (111010), (122414), (133313), (144212)}

and the set of minimal codewords is
{(100111), (111010)}

Therefore, the set {{p3, p4, p5}, {p1, p2, p4}} is a spanning set for the
set of qualiﬁed groups.
    """
    
    html_content = """
    <div class="latex-container">
        <div class="section-title">Complete Example of Massey's Scheme</div>
        
        <div class="content-box">
            <div class="definition-box">
                <p><strong>Code Parameters:</strong></p>
                <div style="display: flex; justify-content: space-around; align-items: center; margin: 20px 0;">
                    <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 8px;">
                        <strong>Linear Code C</strong>
                        <div class="message">[6,4,2] code over F₅</div>
                    </div>
                </div>
            </div>

            <div class="example-box">
                <div class="example-title">Generator and Parity-Check Matrices</div>
                <div style="display: flex; justify-content: space-around; align-items: flex-start; margin: 20px 0;">
                    <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 8px;">
                        <strong>Generator Matrix G</strong>
                        <div class="matrix-display">
                            G = [<br>
                            1 0 0 0 4 0<br>
                            0 1 0 0 4 1<br>
                            1 0 1 0 3 1<br>
                            0 0 0 1 0 4<br>
                            ]
                        </div>
            </div>

                    <div style="text-align: center; padding: 15px; background: #fff3e0; border-radius: 8px;">
                        <strong>Parity-Check Matrix H</strong>
                        <div class="matrix-display">
                            H = [<br>
                            1 0 0 1 1 1<br>
                            0 1 1 4 0 4<br>
                            ]
                        </div>
                    </div>
            </div>
        </div>

        <div class="example-box">
                <div class="example-title">Share Generation</div>
                <div style="display: flex; justify-content: space-around; align-items: flex-start; margin: 20px 0;">
                    <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 8px;">
                        <strong>Input</strong>
                        <div class="message">
                            Secret s = 3 ∈ F₅<br>
                            Vector u = (1,1,2,3)
                        </div>
                    </div>
                    
                    <div style="text-align: center; padding: 15px; background: #fff3e0; border-radius: 8px;">
                        <strong>Computation</strong>
                        <div class="message">
                            t = uG = (3,1,2,3,4,0)
                        </div>
                    </div>
                    
                    <div style="text-align: center; padding: 15px; background: #e8f5e9; border-radius: 8px;">
                        <strong>Shares</strong>
                        <div class="message">
                            t₀ = 3 (secret)<br>
                            t₁ = 1 → p₁<br>
                            t₂ = 2 → p₂<br>
                            t₃ = 3 → p₃<br>
                            t₄ = 4 → p₄<br>
                            t₅ = 0 → p₅
                        </div>
                    </div>
                </div>
        </div>

        <div class="example-box">
                <div class="example-title">Minimal Codewords Analysis</div>
                <div style="display: flex; justify-content: space-around; align-items: flex-start; margin: 20px 0;">
                    <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 8px;">
                        <strong>Codewords with First Coefficient 1</strong>
                        <div class="message">
                            (1,0,0,1,1,1)<br>
                            (1,1,1,0,1,0)<br>
                            (1,2,2,4,1,4)<br>
                            (1,3,3,3,1,3)<br>
                            (1,4,4,2,1,2)
                        </div>
                    </div>
                    
                    <div style="text-align: center; padding: 15px; background: #fff3e0; border-radius: 8px;">
                        <strong>Minimal Codewords</strong>
                        <div class="message">
                            (1,0,0,1,1,1)<br>
                            (1,1,1,0,1,0)
                        </div>
                    </div>
                </div>
        </div>

            <div class="theorem-box">
                <div class="theorem-title">Result</div>
            <p>The spanning set for qualified groups is:</p>
                <div style="text-align: center; padding: 15px; background: #f5f5f5; border-radius: 8px; margin: 10px 0;">
                    <div class="equation">
                        {{p₃, p₄, p₅}, {p₁, p₂, p₄}}
                    </div>
                    <div class="note">These are the minimal qualified groups that can reconstruct the secret</div>
                </div>
            </div>
        </div>
    </div>
    """
    
    display(HTML(html_content))
