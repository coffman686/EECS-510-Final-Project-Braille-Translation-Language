# Braille Translation Language: Theory and Purpose

## Introduction

As our group spent time searching for a language that would accurately surmise all of this semester's teachings concisely, we found that we wanted to create something that could be useful for us, 
and others, down the line. The idea of a Braille translation language came up, so we then moved to further understand the implications of such a language. For us, the idea was to create a language 
that helped the visually unimpaired learn Braille with either a cell phone or some means of accessing our machine.
The idea is to translate Braille into a 3x2 grid of 6 dots, with each dot being a 1, and each gap in the grid being a 0. We can then take those 6 dots, read them left to right, and top to bottom, then put 
them into our machine. Once the machine has read through the dots on the correct path, we can check our dictionary of values and return the letter the person is inputting. 
The intent, for us, is to create a formal grammar that we can use for projects in the future, specifically an application for our capstone project to use an augmented reality environment through 
your phone that takes pictures of Braille, parses them into their grids of 0’s and 1’s, and then reads them back to you. This is further discussed below.
Overarchingly, we want others to be able to empathize with the visually impaired, and perhaps make more efforts to diversify and attempt to change their lives for the better. Plus, learning Braille 
is an excellent skill if you want to communicate with an entirely new world of people!

## Structure of the Language

The structure of our language is meant to read through the entire Braille alphabet, which consists of the 26 letters it shares with the English alphabet. We decided against adding symbols and 
numbers for this project specifically, as we wanted to cover our bases with the letters and thorough comprehension for first-time users of the machine.
The machine operates by proceeding bit by bit through the given binary string, with a loop back to our start state (also our final state) once we have read 6 bits. This is because, regardless 
of what we read, we want to see if the 6 bits we have read match a character in our library, and if they do, we replace the 6 bits with the respective character. If a string contains an invalid 
amount of bits or a combination of binary bits that isn’t in our library, the program will never reach the final state, thus being rejected. 
The smallest string in our language is the empty string, λ, and as such is the only case where the machine won’t attempt to evaluate the input down 6 potential paths. The interconnection of the 
DFA adequately demonstrates that each letter has a specific path the input would follow to inform the user which letter they are reading, with any given input in a situation. If a user is reading 
Braille, the machine returns the letter. If a user enters false strings or inadequate Braille structure, the machine will reject the input and halt.

## Purpose and Impact

In the first paragraph, we briefly touched on the intent behind creating a machine like this, and we will discuss it more broadly in terms of its purpose. The blind make up a population of a 
quarter billion around the world (via the National Library of Medicine). For the number of people afflicted with a disability such as this, it seems there are few resources devoted to learning 
more about this massive subsection of humanity.
For our machine, we wanted to create a new resource for the visually able, to assist in the ongoing quest to empathize and communicate with the visually impaired. A tool such as this being 
utilized as described in our discussion on intent, with an augmented reality setup to scan Braille, could change the relationship between the blind and seeing-eye as we know it.
This, of course, is not some revolutionary idea though. It has been theorized for a long time by empathetic individuals, and it has even been implemented on numerous platforms. 
The difference for us, however, is that we would find ways to market our app and utilize it in a way that teaches the visually unimpaired rather than just giving them a cool tool. 
This could be achieved with some sort of progression in our application environment to give a sense of success and learning and could be figured out later.
The point we wanted to make is that this machine has a higher purpose than just this final project, and our ideation here could create a new method of empathizing with and understanding the 
blind and the issues that they face every day.

## Important Note for Grading

This summary is intended to fufill the requirements for part one of the grading, this is approximately 1.5 pages single spaced and the best summarization of our language possible. 

