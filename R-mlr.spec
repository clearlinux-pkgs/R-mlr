#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mlr
Version  : 2.19.0
Release  : 5
URL      : https://cran.r-project.org/src/contrib/mlr_2.19.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mlr_2.19.0.tar.gz
Summary  : Machine Learning in R
Group    : Development/Tools
License  : BSD-2-Clause
Requires: R-mlr-lib = %{version}-%{release}
Requires: R-BBmisc
Requires: R-ParamHelpers
Requires: R-XML
Requires: R-backports
Requires: R-checkmate
Requires: R-data.table
Requires: R-ggplot2
Requires: R-parallelMap
Requires: R-stringi
BuildRequires : R-BBmisc
BuildRequires : R-ParamHelpers
BuildRequires : R-XML
BuildRequires : R-backports
BuildRequires : R-checkmate
BuildRequires : R-data.table
BuildRequires : R-ggplot2
BuildRequires : R-parallelMap
BuildRequires : R-stringi
BuildRequires : buildreq-R

%description
regression techniques, including machine-readable parameter
    descriptions. There is also an experimental extension for survival
    analysis, clustering and general, example-specific cost-sensitive
    learning. Generic resampling, including cross-validation,
    bootstrapping and subsampling.  Hyperparameter tuning with modern
    optimization techniques, for single- and multi-objective problems.
    Filter and wrapper methods for feature selection. Extension of basic
    learners with additional operations common in machine learning, also
    allowing for easy nested resampling.  Most operations can be
    parallelized.

%package lib
Summary: lib components for the R-mlr package.
Group: Libraries

%description lib
lib components for the R-mlr package.


%prep
%setup -q -c -n mlr
cd %{_builddir}/mlr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641061781

%install
export SOURCE_DATE_EPOCH=1641061781
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mlr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mlr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mlr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc mlr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mlr/CITATION
/usr/lib64/R/library/mlr/DESCRIPTION
/usr/lib64/R/library/mlr/INDEX
/usr/lib64/R/library/mlr/LICENSE
/usr/lib64/R/library/mlr/Meta/Rd.rds
/usr/lib64/R/library/mlr/Meta/data.rds
/usr/lib64/R/library/mlr/Meta/features.rds
/usr/lib64/R/library/mlr/Meta/hsearch.rds
/usr/lib64/R/library/mlr/Meta/links.rds
/usr/lib64/R/library/mlr/Meta/nsInfo.rds
/usr/lib64/R/library/mlr/Meta/package.rds
/usr/lib64/R/library/mlr/Meta/vignette.rds
/usr/lib64/R/library/mlr/NAMESPACE
/usr/lib64/R/library/mlr/NEWS.md
/usr/lib64/R/library/mlr/R/mlr
/usr/lib64/R/library/mlr/R/mlr.rdb
/usr/lib64/R/library/mlr/R/mlr.rdx
/usr/lib64/R/library/mlr/data/Rdata.rdb
/usr/lib64/R/library/mlr/data/Rdata.rds
/usr/lib64/R/library/mlr/data/Rdata.rdx
/usr/lib64/R/library/mlr/doc/index.html
/usr/lib64/R/library/mlr/doc/mlr.R
/usr/lib64/R/library/mlr/doc/mlr.Rmd
/usr/lib64/R/library/mlr/doc/mlr.html
/usr/lib64/R/library/mlr/examples/MultilabelWrapper.R
/usr/lib64/R/library/mlr/help/AnIndex
/usr/lib64/R/library/mlr/help/aliases.rds
/usr/lib64/R/library/mlr/help/mlr.rdb
/usr/lib64/R/library/mlr/help/mlr.rdx
/usr/lib64/R/library/mlr/help/paths.rds
/usr/lib64/R/library/mlr/html/00Index.html
/usr/lib64/R/library/mlr/html/R.css
/usr/lib64/R/library/mlr/makeData.R
/usr/lib64/R/library/mlr/tests/figs/deps.txt
/usr/lib64/R/library/mlr/tests/figs/featsel/feat-type-cols.svg
/usr/lib64/R/library/mlr/tests/figs/featsel/filter-argument.svg
/usr/lib64/R/library/mlr/tests/figs/featsel/n-show-nfeat.svg
/usr/lib64/R/library/mlr/tests/figs/featsel/n-show.svg
/usr/lib64/R/library/mlr/tests/testthat.R
/usr/lib64/R/library/mlr/tests/testthat/Rplots.pdf
/usr/lib64/R/library/mlr/tests/testthat/helper_funs.R
/usr/lib64/R/library/mlr/tests/testthat/helper_helpers.R
/usr/lib64/R/library/mlr/tests/testthat/helper_learners_all.R
/usr/lib64/R/library/mlr/tests/testthat/helper_lint.R
/usr/lib64/R/library/mlr/tests/testthat/helper_mock_learners.R
/usr/lib64/R/library/mlr/tests/testthat/helper_objects.R
/usr/lib64/R/library/mlr/tests/testthat/helper_zzz.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_BaggingWrapper.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_BaseEnsemble.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_BaseWrapper.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_ClassificationViaRegressionWrapper.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_ConstantClassWrapper.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_DummyFeaturesWrapper.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_FailureModel.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_Learner.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_Learner_properties.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_ModelMultiplexer.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_MulticlassWrapper.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_NoFeaturesModel.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_PreprocWrapper.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_PreprocWrapperCaret.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_SupervisedTask.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_TaskDesc.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_TuneWrapper.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_UnsupervisedTask.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_aggregations.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_batchmark.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_benchmark.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_blocking.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_caching.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_calculateConfusionMatrix.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_calculateROCMeasures.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_capLargeValues.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_chains.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_checkData.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_checkTaskLearner.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_checkTaskSubset.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_clustering.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_configureMlr.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_convertBMRToRankMatrix.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_convertMLBenchObjToTask.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_costs.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_costsens.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_createDummyFeatures.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_createSpatialResamplingPlots.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_debugdump.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_downsample.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_dropFeatures.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_estimateResidualVariance.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_fda.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_fda_extractFDAFeatures.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_fda_extractFDAFeaturesMethods.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_fda_extractFDAFeaturesWrapper.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_fixed_indices_cv.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_generateCalibration.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_generateFeatureImportanceData.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_generateHyperParsEffect.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_generateLearningCurve.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_generatePartialDependence.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_generateThreshVsPerf.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_getCaretParamSet.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_getFeatureImportance.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_getHyperPars.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_getOOBPreds.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_getParamSet.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_getTaskData.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_getTaskFormula.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_helpLearner.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_helpers.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_hyperpars.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_imbal_overbagging.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_imbal_overundersample.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_imbal_smote.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_imbal_weightedclasses.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_impute.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_joinClassLevels.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_learnerArgsToControl.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_listLearners.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_makeLearners.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_makeTask.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_measures.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_mergeBenchmarkResults.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_mergeSmallFactorLevels.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_multilabel.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_multilabelWrapperIds.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_normalizeFeatures.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_orderBMRLevels.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_orderedfactors.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_performance.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_plotBMRBoxplots.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_plotBMRRanksAsBarChart.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_plotBMRSummary.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_plotCritDifferences.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_plotLearnerPrediction.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_plotResiduals.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_predict.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_prediction_operators.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_relativeOverfitting.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_removeConstantFeatures.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_resample.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_resample_b632.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_resample_b632plus.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_resample_bs.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_resample_convenience.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_resample_cv.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_resample_fixedwindowcv.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_resample_getResamplingIndices.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_resample_growingwindowcv.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_resample_holdout.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_resample_loo.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_resample_makeResampleDesc.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_resample_operators.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_resample_repcv.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_resample_stratify.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_resample_subsample.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_resample_weights.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_selectFeatures.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_setPredictType.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_simplifyMeasureNames.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_spcv.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_summarizeColumns.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_summarizeLevels.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_train.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_tuneThreshold.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_tuning.R
/usr/lib64/R/library/mlr/tests/testthat/test_base_weights.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_C50.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_FDboost.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_IBk.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_J48.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_JRip.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_LibLineaRMultiClassSVC.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_LiblineaRL1L2SVC.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_LiblineaRL1LogReg.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_LiblineaRL2L1SVC.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_LiblineaRL2LogReg.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_LiblineaRL2SVC.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_OneR.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_PART.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_RRF.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_ada.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_adaboostm1.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_bartMachine.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_binomial.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_boost.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_bst.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_cforest.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_clusterSVM.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_ctree.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_cvglmnet.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_dbnDNN.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_dcSVM.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_earth.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_evtree.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_extraTrees.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_fdausc.glm.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_fdausc.kernel.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_fdausc.knn.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_fdausc.np.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_featureless.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_fgam.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_fnn.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_gamboost.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_gaterSVM.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_gausspr.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_gbm.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_geoDA.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_glmboost.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_glmnet.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_h2odeeplearning.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_h2ogbm.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_h2oglm.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_h2orandomForest.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_kknn.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_knn.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_ksvm.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_lda.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_linDA.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_logreg.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_lssvm.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_mda.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_mlp.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_multinom.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_naiveBayes.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_neuralnet.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_nnTrain.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_nnet.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_nodeHarvest.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_pamr.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_penalized.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_plr.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_plsdaCaret.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_probit.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_qda.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_quaDA.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_rFerns.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_randomForest.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_randomForestSRC.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_ranger.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_rda.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_rknn.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_rotationForest.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_rpart.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_rrlda.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_saeDNN.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_sda.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_sparseLDA.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_svm.R
/usr/lib64/R/library/mlr/tests/testthat/test_classif_xgboost.R
/usr/lib64/R/library/mlr/tests/testthat/test_cluster_Cobweb.R
/usr/lib64/R/library/mlr/tests/testthat/test_cluster_EM.R
/usr/lib64/R/library/mlr/tests/testthat/test_cluster_FarthestFirst.R
/usr/lib64/R/library/mlr/tests/testthat/test_cluster_MiniBatchKmeans.R
/usr/lib64/R/library/mlr/tests/testthat/test_cluster_SimpleKMeans.R
/usr/lib64/R/library/mlr/tests/testthat/test_cluster_XMeans.R
/usr/lib64/R/library/mlr/tests/testthat/test_cluster_cmeans.R
/usr/lib64/R/library/mlr/tests/testthat/test_cluster_dbscan.R
/usr/lib64/R/library/mlr/tests/testthat/test_cluster_kkmeans.R
/usr/lib64/R/library/mlr/tests/testthat/test_cluster_kmeans.R
/usr/lib64/R/library/mlr/tests/testthat/test_featsel_FeatSelWrapper.R
/usr/lib64/R/library/mlr/tests/testthat/test_featsel_FilterWrapper.R
/usr/lib64/R/library/mlr/tests/testthat/test_featsel_analyzeFeatSelResult.R
/usr/lib64/R/library/mlr/tests/testthat/test_featsel_filters.R
/usr/lib64/R/library/mlr/tests/testthat/test_featsel_fselectorrcpp.R
/usr/lib64/R/library/mlr/tests/testthat/test_featsel_generateFilterValuesData.R
/usr/lib64/R/library/mlr/tests/testthat/test_featsel_plotFilterValues.R
/usr/lib64/R/library/mlr/tests/testthat/test_featsel_praznik.R
/usr/lib64/R/library/mlr/tests/testthat/test_featsel_rankSimpleFilters.R
/usr/lib64/R/library/mlr/tests/testthat/test_featsel_selectFeatures.R
/usr/lib64/R/library/mlr/tests/testthat/test_featsel_selectFeaturesSequential.R
/usr/lib64/R/library/mlr/tests/testthat/test_learners_all_classif.R
/usr/lib64/R/library/mlr/tests/testthat/test_learners_all_clusters.R
/usr/lib64/R/library/mlr/tests/testthat/test_learners_all_general.R
/usr/lib64/R/library/mlr/tests/testthat/test_learners_all_multilabel.R
/usr/lib64/R/library/mlr/tests/testthat/test_learners_all_regr.R
/usr/lib64/R/library/mlr/tests/testthat/test_learners_all_surv.R
/usr/lib64/R/library/mlr/tests/testthat/test_learners_classiflabelswitch.R
/usr/lib64/R/library/mlr/tests/testthat/test_lint.R
/usr/lib64/R/library/mlr/tests/testthat/test_multilabel_cforest.R
/usr/lib64/R/library/mlr/tests/testthat/test_multilabel_randomForestSRC.R
/usr/lib64/R/library/mlr/tests/testthat/test_parallel_mpi.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_FDboost.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_GPfit.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_IBk.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_LiblineaRL2L1SVR.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_LiblineaRL2L2SVR.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_RRF.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_bartMachine.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_bcart.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_bgp.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_bgpllm.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_blm.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_brnn.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_bst.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_btgp.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_btgpllm.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_btlm.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_cforest.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_crs.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_ctree.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_cubist.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_cvglmnet.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_earth.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_evtree.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_extraTrees.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_featureless.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_fgam.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_fnn.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_frbs.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_gamboost.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_gausspr.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_gbm.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_glm.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_glmboost.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_glmnet.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_h2odeeplearning.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_h2ogbm.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_h2oglm.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_h2orandomForest.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_kknn.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_km.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_ksvm.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_laGP.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_lm.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_mob.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_nnet.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_nodeHarvest.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_penalized.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_plsr.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_randomForest.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_randomForestSRC.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_ranger.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_rknn.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_rpart.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_rsm.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_svm.R
/usr/lib64/R/library/mlr/tests/testthat/test_regr_xgboost.R
/usr/lib64/R/library/mlr/tests/testthat/test_stack.R
/usr/lib64/R/library/mlr/tests/testthat/test_surv_cforest.R
/usr/lib64/R/library/mlr/tests/testthat/test_surv_coxph.R
/usr/lib64/R/library/mlr/tests/testthat/test_surv_cvglmnet.R
/usr/lib64/R/library/mlr/tests/testthat/test_surv_gamboost.R
/usr/lib64/R/library/mlr/tests/testthat/test_surv_gbm.R
/usr/lib64/R/library/mlr/tests/testthat/test_surv_glmboost.R
/usr/lib64/R/library/mlr/tests/testthat/test_surv_glmnet.R
/usr/lib64/R/library/mlr/tests/testthat/test_surv_measures.R
/usr/lib64/R/library/mlr/tests/testthat/test_surv_randomForestSRC.R
/usr/lib64/R/library/mlr/tests/testthat/test_surv_ranger.R
/usr/lib64/R/library/mlr/tests/testthat/test_surv_rpart.R
/usr/lib64/R/library/mlr/tests/testthat/test_tuneParams.R
/usr/lib64/R/library/mlr/tests/testthat/test_tune_ModelMultiplexer.R
/usr/lib64/R/library/mlr/tests/testthat/test_tune_getTuneResultOptPath.R
/usr/lib64/R/library/mlr/tests/testthat/test_tune_tuneCMAES.R
/usr/lib64/R/library/mlr/tests/testthat/test_tune_tuneDesign.R
/usr/lib64/R/library/mlr/tests/testthat/test_tune_tuneGenSA.R
/usr/lib64/R/library/mlr/tests/testthat/test_tune_tuneGrid.R
/usr/lib64/R/library/mlr/tests/testthat/test_tune_tuneIrace.R
/usr/lib64/R/library/mlr/tests/testthat/test_tune_tuneMBO.R
/usr/lib64/R/library/mlr/tests/testthat/test_tune_tuneParamsMultiCrit.R
/usr/lib64/R/library/mlr/tests/testthat/test_tune_tuneRandom.R
/usr/lib64/R/library/mlr/tests/testthat/test_tune_tuneThreshold.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/mlr/libs/mlr.so
/usr/lib64/R/library/mlr/libs/mlr.so.avx2
/usr/lib64/R/library/mlr/libs/mlr.so.avx512
