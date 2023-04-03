#include <stdio.h>
#include <errno.h>
#include <assert.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <sys/signal.h>
#include <sys/wait.h>
#include <unistd.h>
#include <signal.h>
#include <limits.h>
#include <time.h>


#define MAX 4294967295

#define MAXJOBS 32
#define MAXLINE 1024


typedef struct job {
    pid_t fprocessID;
    pid_t id;
    int job_n;
    char* s;
    char*jobName;
    int status;
    struct job *nextN;
    struct job *prevN;
} job;


int job_count =1 ;

int curr_count = 1;

int fgs = 0;

struct job *headNode = NULL;



char **environ;


void handle_sigchld(int sig) {
    pid_t pID;
    int s;

    while((pID = waitpid(-1 , &s, WNOHANG | WUNTRACED)) > 0 ){
        struct job *c;
        for (c = headNode; c != NULL; c = c->nextN) {
            if (c->id == pID) {
                break;
            }
        }

        if(c != NULL){
            c->status = 0;
            //the child exited normally so it finsihed properly
            if(WIFEXITED(s)){

                c->s = "finished";
                if(c->fprocessID == 0){
                    fprintf(stdout,"[%d] (%d)  %s  %s\n", c->job_n, pID,c->s, c->jobName);
                }else{
                    fgs = 0;
                }

                if (c == headNode) {
                    headNode = c->nextN;
                    if (headNode != NULL) {
                        headNode->prevN = NULL;
                    }
                } else {
                    c->prevN->nextN = c->nextN;
                    if (c->nextN != NULL) {
                        c->nextN->prevN = c->prevN;
                    }
                }
                //removed
                free(c);

                curr_count--;
                //if the process was terminaed using the nuke command
            }else if(WIFSIGNALED(s)){
                if (WCOREDUMP(s)) {
                    c->s = "killed (core dumped)";
                    fgs = 0;
                } else {
                    c->s = "killed";
                }

                fprintf(stdout, "[%d] (%d)  %s  %s\n", c->job_n, pID, c->s, c->jobName);

                if (c == headNode) {
                    headNode = c->nextN;
                    if (headNode != NULL) {
                        headNode->prevN = NULL;
                    }
                } else {
                    c->prevN->nextN = c->nextN;
                    if (c->nextN != NULL) {
                        c->nextN->prevN = c->prevN;
                    }
                }
                //removed
                free(c);

                curr_count--;
                /* fprintf(stdout,"[%d] (%d)  %s  %s\n", c->job_n, pID,c->s, c->jobName); */
                /* curr_count--; */
            }
        }
    }
}



void handle_sigtstp(int sig) {
    // TODO
}

void handle_sigint(int sig) {
    pid_t pID;
    int s;

    struct job *c;
    for (c = headNode; c != NULL; c = c->nextN) {
        if (c->id == pID) {
            break;
        }
    }

    if (c != NULL) {
        if(c->fprocessID == 0){
            kill(c->id, SIGINT);
        }else{
            kill(c->fprocessID, SIGINT);
        }
    }


}

void handle_sigquit(int sig) {

    pid_t pID;
    int s;

    struct job *c;
    for (c = headNode; c != NULL; c = c->nextN) {
        if (c->id == pID) {
            break;
        }
    }

    if(fgs == 1){
        struct job *c;
        for (c = headNode; c != NULL; c = c->nextN) {
            if (c->id == pID) {
                break;
            }
        }


        if (c != NULL) {
            if(c->fprocessID == 0){
                kill(c->id, SIGQUIT);
            }else{
                kill(c->fprocessID, SIGQUIT);
            }
        }
    }
    else {
        exit(0);
    }
}

void install_signal_handlers() {
    //sigchild
    struct sigaction siga;
    siga.sa_handler = &handle_sigchld;
    siga.sa_flags = SA_RESTART;
    sigemptyset(&siga.sa_mask);
    sigaddset(&siga.sa_mask, SIGCHLD);
    sigaction(SIGCHLD, &siga, NULL);
    //sigquit
    struct sigaction siga1;
    siga1.sa_handler = &handle_sigquit;
    siga1.sa_flags = SA_RESTART;
    sigemptyset(&siga1.sa_mask);
    sigaddset(&siga1.sa_mask, SIGQUIT);
    sigaction(SIGQUIT, &siga1, NULL);
    //sigstp
    struct sigaction siga2;
    siga2.sa_handler = &handle_sigtstp;
    siga2.sa_flags = SA_RESTART;
    sigemptyset(&siga2.sa_mask);
    sigaddset(&siga2.sa_mask, SIGTSTP);
    sigaction(SIGTSTP, &siga2, NULL);
    //sigint
    struct sigaction siga3;
    siga3.sa_handler = &handle_sigint;
    siga3.sa_flags = SA_RESTART;
    sigemptyset(&siga3.sa_mask);
    sigaddset(&siga3.sa_mask, SIGINT);
    sigaction(SIGINT, &siga3, NULL);
}

void spawn(const char **toks, bool bg) { // bg is true iff command ended with &
                                         //spawn a child which will do the actual spawn
    if(bg == true){
        if(curr_count > MAXJOBS){
            fprintf(stderr,"ERROR: too many jobs\n");
            return;
        }
        //setup the
        sigset_t m;
        sigemptyset(&m);
        sigaddset(&m, SIGCHLD);
        //block the sigchild signal for the parent so theres no race conditions
        sigprocmask(SIG_BLOCK, &m, NULL);


        if(curr_count <=  MAXJOBS){
            //make child process run command
            pid_t pID = fork();
            if(pID == 0){
                sigprocmask(SIG_UNBLOCK, &m, NULL);
                execvp(toks[0], (char **) toks);
                fprintf(stderr, "ERROR: cannot run %s\n", strdup(toks[0]));
                exit(0);
            }
            else if(pID > 0){
                // can set up a signal handler here if we need
                //reap any zombie processes
                int status;
                struct job *nj = malloc(sizeof(job));
                nj->id = pID;
                nj->status = 1;
                nj->fprocessID = 0;
                nj->s = "running";
                curr_count++;
                nj->job_n = job_count;
                job_count++;
                //get the name of the job
                nj->jobName = strdup(toks[0]);
                //put this new job into the jobs linked list
                nj->nextN = NULL;
                //if its the first job
                if(headNode == NULL){
                    nj->prevN = NULL;
                    headNode = nj;
                }
                else if(headNode != NULL){
                    struct job *curr = headNode;
                    while(curr->nextN != NULL){
                        curr = curr->nextN;
                    }
                    //add the new job to the end of the linked list
                    curr->nextN = nj;
                    nj->prevN = curr;
                }
                //Unblocks the sigchild for the parent process
                //now the parent can reap or see if the child has died and actually knows the state of the child process
                printf("[%d] (%d)  %s  %s \n", nj->job_n , nj->id, nj->s , toks[0]);
                fflush(stdout);
                sigprocmask(SIG_UNBLOCK, &m, NULL);
                //now check for dead children
            }
            else{
                perror("ERROR");
                return;
            }
        }
    }else{
        //setup the masking for the signals
        sigset_t m;
        sigemptyset(&m);
        sigaddset(&m, SIGCHLD);
        //block the sigchild signal for the parent so theres no race conditions
        sigaddset(&m, SIGINT);
        sigaddset(&m, SIGQUIT);
        sigprocmask(SIG_BLOCK, &m, NULL);

        //now make the child process which will run the fg process
        pid_t fprocess = fork();
        if(fprocess == 0){
            sigprocmask(SIG_UNBLOCK, &m, NULL);
            execvp(toks[0], (char **) toks);
            fprintf(stderr, "ERROR: cannot run %s\n", strdup(toks[0]));
            exit(0);

        }else if (fprocess > 0) {
            struct job *nfj = malloc(sizeof(job));
            nfj->id = fprocess;
            nfj->status = 1;
            nfj->fprocessID = fprocess;
            nfj->s = "running";
            fgs = 1;
            curr_count++;
            nfj->job_n = job_count;
            job_count++;
            nfj->jobName = strdup(toks[0]);

            nfj->nextN = NULL;
            //if its the first job
            if(headNode == NULL){
                nfj->prevN = NULL;
                headNode = nfj;
            }
            else if(headNode != NULL){
                struct job *curr = headNode;
                while(curr->nextN != NULL){
                    curr = curr->nextN;
                }
                //add the new job to the end of the linked list
                curr->nextN = nfj;
                nfj->prevN = curr;
            }


            //now unblock the signal and check if the fg process is done
            sigprocmask(SIG_UNBLOCK, &m, NULL);
            while(strcmp(nfj->s, "running") == 0){
                struct timespec ts;
                //sleep for 1 ms
                ts.tv_nsec = 1000000;
                nanosleep(&ts, NULL);
                if(strcmp(nfj->s, "finished") == 0){
                    break;
                }
            }


        }
    }
}


void cmd_jobs(const char **toks) {

    if (toks[1] != NULL) {
        fprintf(stderr, "ERROR: jobs takes no arguments\n");
    } else {
        //print all the jobs
        struct job* c = headNode;
        while(c != NULL){
            if(strcmp(c->s, "running") == 0){
                fprintf(stdout, "[%d] (%d)  %s  %s\n", c->job_n, c->id, c->s, c->jobName);
            }
            c = c->nextN;

        }
    }
}









void cmd_fg(const char **toks) {
    if(toks[2] != NULL){
        printf("ERROR: fg takes exactly one argument\n");
        fflush(stdout);
        return;
    }
    if(toks[1] == NULL){
        fprintf(stderr, "ERROR: fg takes exactly one argument\n");
        return;
    }else{
        if(toks[1][0] == '%'){
            char* temp;
            errno = 0;
            long p;
            if (toks[1][0] == '%') {
                p = strtol(toks[1] + 1, &temp, 10);
            }

            if (*temp != '\0' || errno == ERANGE || p > INT_MAX) {
                fprintf(stderr, "ERROR: bad argument for fg: %s\n", toks[1]);
                return;
            }
            sigset_t m;
            sigemptyset(&m);
            sigaddset(&m, SIGCHLD);
            sigaddset(&m, SIGINT);
            sigaddset(&m, SIGQUIT);
            sigaddset(&m, SIGTSTP);

            sigprocmask(SIG_BLOCK, &m, NULL);
            struct job *c;
            int found = 0;
            for (c = headNode; c != NULL; c = c->nextN) {
                //no need to handle the sigkill signal since os does that for unistd
                if(c->job_n == p){
                    sigprocmask(SIG_UNBLOCK, &m, NULL);
                    //now put this job to the foregound!!!!!!!!!!
                    if (strcmp(c->s, "running") == 0) {

                        found = 1;
                        c->fprocessID = c->id;
                        fgs = 1;
                        while(strcmp(c->s, "running") == 0){
                            struct timespec ts;
                            //sleep for 1 ms
                            ts.tv_nsec = 1000000;
                            nanosleep(&ts, NULL);
                            if(strcmp(c->s, "finished") == 0){
                                break;
                            }
                        }
                    }else if(strcmp(c->s, "suspended") == 0){
                        found = 1;
                        c->fprocessID = c->id;
                        sigprocmask(SIG_UNBLOCK, &m, NULL);
                        c->s = "running";
                        fprintf(stdout, "[%d] (%d)  %s  %s\n", c->job_n, c->id, c->s, c->jobName);
                        kill(c->id, SIGCONT);
                        fgs = 1;
                        while(strcmp(c->s, "running") == 0  ){
                            struct timespec ts;
                            //sleep for 1 ms
                            ts.tv_nsec = 1000000;
                            nanosleep(&ts, NULL);
                            if(strcmp(c->s, "finished") == 0 || strcmp(c->s, "suspended") == 0){
                                break;
                            }
                        }
                    }
                }
            }

            if(!found){
                fprintf(stderr, "ERROR: job %s\n", toks[1]);
            }


        }else {
            char* temp;
            errno = 0;
            long p = strtol(toks[1],&temp, 10);
            if (*temp != '\0' || errno == ERANGE || p > INT_MAX) {
                fprintf(stderr, "ERROR: bad argument for fg: %s\n", toks[1]);
                return;
            }

            sigset_t m;
            sigemptyset(&m);
            sigaddset(&m, SIGCHLD);
            sigaddset(&m, SIGINT);
            sigaddset(&m, SIGQUIT);
            sigaddset(&m, SIGTSTP);
            sigprocmask(SIG_BLOCK, &m, NULL);
            struct job *c;
            int found = 0;
            for (c = headNode; c != NULL; c = c->nextN) {
                //no need to handle the sigkill signal since os does that for unistd
                if(c->id == p){
                    sigprocmask(SIG_UNBLOCK, &m, NULL);
                    //now put this job to the foregound!!!!!!!!!!
                    if (strcmp(c->s, "running") == 0) {
                        c->fprocessID = c->id;
                        fgs = 1;
                        found = 1;
                        while(strcmp(c->s, "running") == 0){
                            struct timespec ts;
                            //sleep for 1 ms
                            ts.tv_nsec = 1000000;
                            nanosleep(&ts, NULL);
                            if(strcmp(c->s, "finished") == 0){
                                break;
                            }
                        }
                    }else if(strcmp(c->s, "suspended") == 0){
                        c->fprocessID = c->id;
                        fgs = 1;
                        found = 1;
                        kill(c->id, SIGCONT);
                        while(strcmp(c->s, "running") == 0  ){
                            struct timespec ts;
                            //sleep for 1 ms
                            ts.tv_nsec = 1000000;
                            nanosleep(&ts, NULL);
                            if(strcmp(c->s, "finished") == 0 || strcmp(c->s, "suspended") == 0){
                                break;
                            }
                        }
                    }

                }
            }
            if(!found){
                fprintf(stderr, "ERROR: no PID %s\n", toks[1]);
            }

        }
    }
}



















void cmd_bg(const char **toks) {
    // TODO
}




void cmd_nuke(const char **toks) {
    //if specific job is being targeted
    if(toks[2] != NULL){
        fprintf(stderr, "ERROR: nuke takes exactly one argument\n");
        return;
        //nuke a specified job
    }else if(toks[1] != NULL){
        //arg is the job number
        if(toks[1][0] == '%'){
            char* temp;
            errno = 0;
            long p;
            if (toks[1][0] == '%') {
                p = strtol(toks[1] + 1, &temp, 10);
            }

            if (*temp != '\0' || errno == ERANGE || p > MAX) {
                fprintf(stderr, "ERROR: bad argument for nuke: %s\n", toks[1]);
                return;
            }

            struct job *c;
            int found = 0;
            for (c = headNode; c != NULL; c = c->nextN) {
                //no need to handle the sigkill signal since os does that for unistd
                if(c->job_n == p){
                    found = 1;
                    kill(c->id, SIGKILL);
                }
            }

            if(!found){
                fprintf(stderr, "ERROR: no job %s\n", toks[1]);
            }


            //arg is the PID
        }else {
            char* temp;
            errno = 0;
            long p = strtol(toks[1],&temp, 10);
            if (*temp != '\0' || errno == ERANGE || p > MAX) {
                fprintf(stderr, "ERROR: bad argument for nuke: %s\n", toks[1]);
                return;
            }

            struct job *c;
            int found = 0;
            for (c = headNode; c != NULL; c = c->nextN) {
                //no need to handle the sigkill signal since os does that for unistd
                if(strtol(toks[1], NULL, 10) == c->id){
                    found = 1;
                    kill(c->id, SIGKILL);
                }
            }

            if(!found){
                fprintf(stderr, "ERROR: no PID %s\n", toks[1]);
            }

        }
    }else{
        struct job *c;
        for (c = headNode; c != NULL; c = c->nextN) {
            //no need to handle the sigkill signal since os does that for unistd
            if(strcmp(c->s, "running") == 0){
                kill(c->id, SIGKILL);
            }
        }

    }
}



void cmd_quit(const char **toks) {
    if (toks[1] != NULL) {
        fprintf(stderr, "ERROR: quit takes no arguments\n");
    } else {
        exit(0);
    }
}

void eval(const char **toks, bool bg) { // bg is true iff command ended with &
    assert(toks);
    if (*toks == NULL){
        return;
    }
    if (strcmp(toks[0], "quit") == 0) {
        cmd_quit(toks);
    } else if( strcmp(toks[0], "jobs") == 0){
        cmd_jobs(toks);
    }
    else if (strcmp(toks[0], "nuke") == 0){
        cmd_nuke(toks);
    }
    else if (strcmp(toks[0], "fg") == 0) {
        cmd_fg(toks);
    }
    else {
        spawn(toks, bg);
    }
}

// you don't need to touch this unless you want to add debugging
void parse_and_eval(char *s) {
    assert(s);
    const char *toks[MAXLINE + 1];

    while (*s != '\0') {
        bool end = false;
        bool bg = false;
        int t = 0;

        while (*s != '\0' && !end) {
            while (*s == '\n' || *s == '\t' || *s == ' ') ++s;
            if (*s != ';' && *s != '&' && *s != '\0') toks[t++] = s;
            while (strchr("&;\n\t ", *s) == NULL) ++s;
            switch (*s) {
                case '&':
                    bg = true;
                    end = true;
                    break;
                case ';':
                    end = true;
                    break;
            }
            if (*s) *s++ = '\0';
        }
        toks[t] = NULL;
        eval(toks, bg);
    }
}

// you don't need to touch this unless you want to add debugging
void prompt() {
    printf("crash> ");
    fflush(stdout);
}

// you don't need to touch this unless you want to add debugging
int repl() {
    char *buf = NULL;
    size_t len = 0;
    while (prompt(), getline(&buf, &len, stdin) != -1) {
        parse_and_eval(buf);
    }

    if (buf != NULL) free(buf);
    if (ferror(stdin)) {
        perror("ERROR");
        return 1;
    }
    return 0;
}

// you don't need to touch this unless you want to add debugging options
int main(int argc, char **argv) {
    install_signal_handlers();
    return repl();
}
