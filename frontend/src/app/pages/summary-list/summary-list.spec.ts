import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SummaryList } from './summary-list.component';

describe('SummaryList', () => {
  let component: SummaryList;
  let fixture: ComponentFixture<SummaryList>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SummaryList]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SummaryList);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
