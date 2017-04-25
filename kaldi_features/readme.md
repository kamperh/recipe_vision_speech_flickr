Extract Speech Features Using Kaldi
===================================

After updating the paths in these files, run:

    source cmd.sh
    source path.sh

Prepare format for Kaldi feature extraction:

    ./flickr8k_data_prep_vad.py

Extract filterbank features:

    ./steps/make_fbank.sh --compress false --nj 30 --cmd "$train_cmd" \
        data/full_vad exp/make_fbank/full_vad fbank
    cat fbank/raw_fbank_full_vad.*.scp > fbank/fbank_full_vad.scp

The `--nj` argument specifies the number of CPU cores to use.

Extract MFCC features:

    ./steps/make_mfcc.sh --nj 30 --cmd "$train_cmd" data/full_vad \
        exp/make_mfcc/full_vad mfcc
    ./steps/compute_cmvn_stats.sh data/full_vad exp/make_mfcc/full_vad mfcc
    ./local/cmvn_dd.sh --nj 30 --cmd "$train_cmd" data/full_vad \
        exp/make_cmvn_dd/full_vad mfcc
    cat mfcc/mfcc_cmnv_dd_full_vad.*.scp > mfcc/mfcc_cmnv_dd_full_vad.scp

Get duration of complete corpus:

    cat data/full_vad/segments | \
        awk 'BEGIN {sum = 0.0} {sum += $4 - $3} \
        END {printf "Total duration: %.6f hours\n", sum/60.0/60.0}'
