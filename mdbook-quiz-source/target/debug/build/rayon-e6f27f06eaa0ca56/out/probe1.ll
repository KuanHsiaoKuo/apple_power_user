; ModuleID = 'probe1.49aa193e-cgu.0'
source_filename = "probe1.49aa193e-cgu.0"
target datalayout = "e-m:o-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-apple-macosx10.7.0"

%"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>" = type { i64, { i32, i32 }, i8, [7 x i8] }
%"core::iter::adapters::rev::Rev<core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>>" = type { %"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>" }
%"core::panic::location::Location" = type { { [0 x i8]*, i64 }, i32, i32 }
%"unwind::libunwind::_Unwind_Exception" = type { i64, void (i32, %"unwind::libunwind::_Unwind_Exception"*)*, [6 x i64] }
%"unwind::libunwind::_Unwind_Context" = type { [0 x i8] }

@alloc19 = private unnamed_addr constant <{ [27 x i8] }> <{ [27 x i8] c"assertion failed: step != 0" }>, align 1
@alloc20 = private unnamed_addr constant <{ [89 x i8] }> <{ [89 x i8] c"/rustc/7737e0b5c4103216d6fd8cf941b7ab9bdbaace7c/library/core/src/iter/adapters/step_by.rs" }>, align 1
@alloc21 = private unnamed_addr constant <{ i8*, [16 x i8] }> <{ i8* getelementptr inbounds (<{ [89 x i8] }>, <{ [89 x i8] }>* @alloc20, i32 0, i32 0, i32 0), [16 x i8] c"Y\00\00\00\00\00\00\00\15\00\00\00\09\00\00\00" }>, align 8

; probe1::probe
; Function Attrs: uwtable
define void @_ZN6probe15probe17h88659a1cd765b415E() unnamed_addr #0 {
start:
  %_3 = alloca { i32, i32 }, align 4
  %_2 = alloca %"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>", align 8
  %_1 = alloca %"core::iter::adapters::rev::Rev<core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>>", align 8
  %0 = bitcast { i32, i32 }* %_3 to i32*
  store i32 0, i32* %0, align 4
  %1 = getelementptr inbounds { i32, i32 }, { i32, i32 }* %_3, i32 0, i32 1
  store i32 10, i32* %1, align 4
  %2 = getelementptr inbounds { i32, i32 }, { i32, i32 }* %_3, i32 0, i32 0
  %3 = load i32, i32* %2, align 4
  %4 = getelementptr inbounds { i32, i32 }, { i32, i32 }* %_3, i32 0, i32 1
  %5 = load i32, i32* %4, align 4
; call core::iter::traits::iterator::Iterator::step_by
  call void @_ZN4core4iter6traits8iterator8Iterator7step_by17h7b231c45fd3c3832E(%"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>"* noalias nocapture noundef sret(%"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>") dereferenceable(24) %_2, i32 %3, i32 %5, i64 2)
  br label %bb1

bb1:                                              ; preds = %start
; call core::iter::traits::iterator::Iterator::rev
  call void @_ZN4core4iter6traits8iterator8Iterator3rev17h514a521d5d576ec1E(%"core::iter::adapters::rev::Rev<core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>>"* noalias nocapture noundef sret(%"core::iter::adapters::rev::Rev<core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>>") dereferenceable(24) %_1, %"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>"* noalias nocapture noundef dereferenceable(24) %_2)
  br label %bb2

bb2:                                              ; preds = %bb1
  ret void
}

; core::iter::adapters::rev::Rev<T>::new
; Function Attrs: uwtable
define void @"_ZN4core4iter8adapters3rev12Rev$LT$T$GT$3new17h20a144ba6bd5c7d5E"(%"core::iter::adapters::rev::Rev<core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>>"* noalias nocapture noundef sret(%"core::iter::adapters::rev::Rev<core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>>") dereferenceable(24) %0, %"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>"* noalias nocapture noundef dereferenceable(24) %iter) unnamed_addr #0 {
start:
  %_2 = alloca %"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>", align 8
  %1 = bitcast %"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>"* %_2 to i8*
  %2 = bitcast %"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>"* %iter to i8*
  call void @llvm.memcpy.p0i8.p0i8.i64(i8* align 8 %1, i8* align 8 %2, i64 24, i1 false)
  %3 = bitcast %"core::iter::adapters::rev::Rev<core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>>"* %0 to %"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>"*
  %4 = bitcast %"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>"* %3 to i8*
  %5 = bitcast %"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>"* %_2 to i8*
  call void @llvm.memcpy.p0i8.p0i8.i64(i8* align 8 %4, i8* align 8 %5, i64 24, i1 false)
  ret void
}

; core::iter::adapters::step_by::StepBy<I>::new
; Function Attrs: uwtable
define void @"_ZN4core4iter8adapters7step_by15StepBy$LT$I$GT$3new17h623bde78ee7743b1E"(%"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>"* noalias nocapture noundef sret(%"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>") dereferenceable(24) %0, i32 %iter.0, i32 %iter.1, i64 %step) unnamed_addr #0 personality i32 (i32, i32, i64, %"unwind::libunwind::_Unwind_Exception"*, %"unwind::libunwind::_Unwind_Context"*)* @rust_eh_personality {
start:
  %1 = alloca { i8*, i32 }, align 8
  %_4 = icmp ne i64 %step, 0
  %_3 = xor i1 %_4, true
  br i1 %_3, label %bb1, label %bb2

bb2:                                              ; preds = %start
  %_7 = sub i64 %step, 1
  %2 = getelementptr inbounds %"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>", %"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>"* %0, i32 0, i32 1
  %3 = getelementptr inbounds { i32, i32 }, { i32, i32 }* %2, i32 0, i32 0
  store i32 %iter.0, i32* %3, align 8
  %4 = getelementptr inbounds { i32, i32 }, { i32, i32 }* %2, i32 0, i32 1
  store i32 %iter.1, i32* %4, align 4
  %5 = bitcast %"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>"* %0 to i64*
  store i64 %_7, i64* %5, align 8
  %6 = getelementptr inbounds %"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>", %"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>"* %0, i32 0, i32 2
  store i8 1, i8* %6, align 8
  ret void

bb1:                                              ; preds = %start
; invoke core::panicking::panic
  invoke void @_ZN4core9panicking5panic17hdb1992cacba5f03aE([0 x i8]* noundef nonnull align 1 bitcast (<{ [27 x i8] }>* @alloc19 to [0 x i8]*), i64 27, %"core::panic::location::Location"* noundef align 8 dereferenceable(24) bitcast (<{ i8*, [16 x i8] }>* @alloc21 to %"core::panic::location::Location"*)) #4
          to label %unreachable unwind label %cleanup

unreachable:                                      ; preds = %bb1
  unreachable

bb3:                                              ; preds = %cleanup
  br label %bb4

cleanup:                                          ; preds = %bb1
  %7 = landingpad { i8*, i32 }
          cleanup
  %8 = extractvalue { i8*, i32 } %7, 0
  %9 = extractvalue { i8*, i32 } %7, 1
  %10 = getelementptr inbounds { i8*, i32 }, { i8*, i32 }* %1, i32 0, i32 0
  store i8* %8, i8** %10, align 8
  %11 = getelementptr inbounds { i8*, i32 }, { i8*, i32 }* %1, i32 0, i32 1
  store i32 %9, i32* %11, align 8
  br label %bb3

bb4:                                              ; preds = %bb3
  %12 = bitcast { i8*, i32 }* %1 to i8**
  %13 = load i8*, i8** %12, align 8
  %14 = getelementptr inbounds { i8*, i32 }, { i8*, i32 }* %1, i32 0, i32 1
  %15 = load i32, i32* %14, align 8
  %16 = insertvalue { i8*, i32 } undef, i8* %13, 0
  %17 = insertvalue { i8*, i32 } %16, i32 %15, 1
  resume { i8*, i32 } %17
}

; core::iter::traits::iterator::Iterator::step_by
; Function Attrs: inlinehint uwtable
define void @_ZN4core4iter6traits8iterator8Iterator7step_by17h7b231c45fd3c3832E(%"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>"* noalias nocapture noundef sret(%"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>") dereferenceable(24) %0, i32 %self.0, i32 %self.1, i64 %step) unnamed_addr #1 {
start:
; call core::iter::adapters::step_by::StepBy<I>::new
  call void @"_ZN4core4iter8adapters7step_by15StepBy$LT$I$GT$3new17h623bde78ee7743b1E"(%"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>"* noalias nocapture noundef sret(%"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>") dereferenceable(24) %0, i32 %self.0, i32 %self.1, i64 %step)
  br label %bb1

bb1:                                              ; preds = %start
  ret void
}

; core::iter::traits::iterator::Iterator::rev
; Function Attrs: inlinehint uwtable
define void @_ZN4core4iter6traits8iterator8Iterator3rev17h514a521d5d576ec1E(%"core::iter::adapters::rev::Rev<core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>>"* noalias nocapture noundef sret(%"core::iter::adapters::rev::Rev<core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>>") dereferenceable(24) %0, %"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>"* noalias nocapture noundef dereferenceable(24) %self) unnamed_addr #1 {
start:
  %_2 = alloca %"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>", align 8
  %1 = bitcast %"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>"* %_2 to i8*
  %2 = bitcast %"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>"* %self to i8*
  call void @llvm.memcpy.p0i8.p0i8.i64(i8* align 8 %1, i8* align 8 %2, i64 24, i1 false)
; call core::iter::adapters::rev::Rev<T>::new
  call void @"_ZN4core4iter8adapters3rev12Rev$LT$T$GT$3new17h20a144ba6bd5c7d5E"(%"core::iter::adapters::rev::Rev<core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>>"* noalias nocapture noundef sret(%"core::iter::adapters::rev::Rev<core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>>") dereferenceable(24) %0, %"core::iter::adapters::step_by::StepBy<core::ops::range::Range<i32>>"* noalias nocapture noundef dereferenceable(24) %_2)
  br label %bb1

bb1:                                              ; preds = %start
  ret void
}

; Function Attrs: argmemonly nofree nounwind willreturn
declare void @llvm.memcpy.p0i8.p0i8.i64(i8* noalias nocapture writeonly, i8* noalias nocapture readonly, i64, i1 immarg) #2

; Function Attrs: uwtable
declare i32 @rust_eh_personality(i32, i32, i64, %"unwind::libunwind::_Unwind_Exception"*, %"unwind::libunwind::_Unwind_Context"*) unnamed_addr #0

; core::panicking::panic
; Function Attrs: cold noinline noreturn uwtable
declare void @_ZN4core9panicking5panic17hdb1992cacba5f03aE([0 x i8]* noundef nonnull align 1, i64, %"core::panic::location::Location"* noundef align 8 dereferenceable(24)) unnamed_addr #3

attributes #0 = { uwtable "frame-pointer"="all" "probe-stack"="__rust_probestack" "target-cpu"="core2" }
attributes #1 = { inlinehint uwtable "frame-pointer"="all" "probe-stack"="__rust_probestack" "target-cpu"="core2" }
attributes #2 = { argmemonly nofree nounwind willreturn }
attributes #3 = { cold noinline noreturn uwtable "frame-pointer"="all" "probe-stack"="__rust_probestack" "target-cpu"="core2" }
attributes #4 = { noreturn }

!llvm.module.flags = !{!0}

!0 = !{i32 7, !"PIC Level", i32 2}
